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

            try:
                # Use ADK agent's built-in streaming (handles tools automatically)
                # ADK agents use their instruction and tools internally
                from google.adk.runners import run_agent

                # Create context with message
                context = {"user_message": message}

                # Run agent asynchronously with streaming
                async for event in run_agent(adk_agent, context=context, stream=True):
                    # Handle different event types from ADK
                    if hasattr(event, 'text') and event.text:
                        full_response += event.text
                        yield {
                            "type": "chunk",
                            "content": event.text,
                            "agent": agent_name
                        }
                    elif hasattr(event, 'tool_call'):
                        # Show tool execution to user
                        yield {
                            "type": "chunk",
                            "content": f"\n[Calling tool: {event.tool_call.name}]\n",
                            "agent": agent_name
                        }

            except Exception as e:
                logger.error(f"ADK agent execution error: {str(e)}")
                # Fallback to direct genai call if ADK streaming fails
                from google import genai
                client = genai.Client(api_key=settings.google_api_key)

                response = await client.aio.models.generate_content_stream(
                    model=adk_agent.model,
                    contents=[{"role": "user", "parts": [{"text": message}]}],
                    config={"tools": adk_agent.tools} if hasattr(adk_agent, 'tools') and adk_agent.tools else None
                )

                async for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        yield {
                            "type": "chunk",
                            "content": chunk.text,
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
