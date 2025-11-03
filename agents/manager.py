"""
Agent Manager - Integrates ADK agents with FastAPI
Loads agents from adk_agents/ and makes them available via WebSocket
"""
import logging
import sys
import importlib
from pathlib import Path
from typing import Dict, List, Optional, AsyncGenerator
from config.settings import settings

logger = logging.getLogger(__name__)

class AgentManager:
    """Manages ADK agents for FastAPI integration"""

    def __init__(self):
        self.agents: Dict[str, any] = {}
        self.sessions: Dict[str, List] = {}  # In-memory session store

    async def initialize(self):
        """Initialize the agent manager and load ADK agents"""
        try:
            # Add adk_agents to Python path
            adk_agents_path = Path(__file__).parent.parent / "adk_agents"
            sys.path.insert(0, str(adk_agents_path))

            # Auto-discover agents from adk_agents/ directory
            discovered_agents = self._discover_agents(adk_agents_path)
            logger.info(f"Discovered {len(discovered_agents)} agents: {discovered_agents}")

            # Load each discovered agent
            for agent_name in discovered_agents:
                await self._load_adk_agent(agent_name)

            logger.info("Agent manager initialized successfully")
            logger.info(f"Loaded {len(self.agents)} ADK agents: {list(self.agents.keys())}")
        except Exception as e:
            logger.error(f"Failed to initialize agent manager: {str(e)}")
            raise

    def _discover_agents(self, adk_agents_path: Path) -> List[str]:
        """Discover all valid ADK agents in adk_agents/ directory

        An agent is valid if:
        1. It's a directory in adk_agents/
        2. It contains agent.py file
        3. The agent.py file exports a 'root_agent' variable

        Args:
            adk_agents_path: Path to adk_agents directory

        Returns:
            List of agent names (directory names)
        """
        agents = []

        if not adk_agents_path.exists():
            logger.warning(f"ADK agents path not found: {adk_agents_path}")
            return agents

        for item in adk_agents_path.iterdir():
            # Skip hidden directories and __pycache__
            if not item.is_dir() or item.name.startswith('_') or item.name.startswith('.'):
                continue

            # Check for agent.py file
            agent_file = item / "agent.py"
            if not agent_file.exists():
                logger.debug(f"Skipping {item.name}: no agent.py found")
                continue

            # Verify it exports root_agent (simple text search)
            try:
                content = agent_file.read_text()
                if 'root_agent' in content:
                    agents.append(item.name)
                    logger.debug(f"Discovered agent: {item.name}")
                else:
                    logger.debug(f"Skipping {item.name}: no root_agent variable")
            except Exception as e:
                logger.warning(f"Error checking {item.name}: {e}")

        return sorted(agents)  # Alphabetical order

    async def _load_adk_agent(self, agent_name: str):
        """Load an ADK agent from adk_agents/ directory"""
        try:
            # Import the actual ADK agent module
            # Now that Starlette conflict is fixed, we can import ADK directly
            module_path = f"{agent_name}.agent"
            agent_module = importlib.import_module(module_path)

            # Get the root_agent object
            if not hasattr(agent_module, 'root_agent'):
                raise AttributeError(f"Agent module {agent_name} missing 'root_agent'")

            root_agent = agent_module.root_agent

            # Store the actual ADK agent object
            self.agents[agent_name] = root_agent
            logger.info(f"Loaded ADK agent: {agent_name}")

        except Exception as e:
            logger.error(f"Failed to load agent {agent_name}: {str(e)}")
            raise

    
    async def stream_chat(
        self,
        session_id: str,
        message: str,
        agent_name: str = "greeting_agent"
    ) -> AsyncGenerator[Dict, None]:
        """Stream chat responses from an ADK agent with tool support"""
        try:
            # Get the actual ADK agent object
            if agent_name not in self.agents:
                yield {"error": f"Agent '{agent_name}' not found. Available: {list(self.agents.keys())}"}
                return

            adk_agent = self.agents[agent_name]

            # Get or create session history
            if session_id not in self.sessions:
                self.sessions[session_id] = []

            # ADK agents handle their own system instructions and tools
            # Just pass the user message
            full_response = ""

            # Use genai directly with agent's configuration
            # ADK agents are declarative - we extract their config and execute
            from google import genai
            from google.genai import types

            try:
                client = genai.Client(api_key=settings.google_api_key)

                # Build the content with agent's instruction as system
                contents = []

                # Add history if exists
                if self.sessions[session_id]:
                    contents = self.sessions[session_id].copy()

                # Add new user message with current date context
                from datetime import datetime
                current_date = datetime.now().strftime("%B %d, %Y")

                # First message includes date context
                if not self.sessions[session_id]:
                    message_with_context = f"Today's date is {current_date}.\n\nUser question: {message}"
                else:
                    message_with_context = message

                contents.append(types.Content(
                    role="user",
                    parts=[types.Part(text=message_with_context)]
                ))

                # Prepare config for tools (if agent has them)
                config = None
                if hasattr(adk_agent, 'tools') and adk_agent.tools:
                    config = types.GenerateContentConfig(
                        system_instruction=adk_agent.instruction if hasattr(adk_agent, 'instruction') else None,
                        tools=adk_agent.tools
                    )
                elif hasattr(adk_agent, 'instruction'):
                    config = types.GenerateContentConfig(
                        system_instruction=adk_agent.instruction
                    )

                # Get model name
                model_name = adk_agent.model if hasattr(adk_agent, 'model') else "gemini-2.0-flash-exp"

                # Stream response (await the coroutine first)
                response_stream = await client.aio.models.generate_content_stream(
                    model=model_name,
                    contents=contents,
                    config=config
                )

                async for chunk in response_stream:
                    if chunk.text:
                        full_response += chunk.text
                        yield {
                            "type": "chunk",
                            "content": chunk.text,
                            "agent": agent_name
                        }

            except Exception as e:
                logger.error(f"Agent execution error: {str(e)}")
                yield {
                    "type": "chunk",
                    "content": f"Error: {str(e)}",
                    "agent": agent_name
                }

            # Store in session history
            self.sessions[session_id].append({
                "role": "user",
                "content": message
            })
            self.sessions[session_id].append({
                "role": "assistant",
                "content": full_response
            })

            yield {
                "type": "complete",
                "agent": agent_name
            }

        except Exception as e:
            logger.error(f"Stream chat error: {str(e)}")
            yield {"error": str(e)}
    
    async def cleanup(self):
        """Cleanup resources"""
        self.sessions.clear()
        logger.info("Agent manager cleaned up")
