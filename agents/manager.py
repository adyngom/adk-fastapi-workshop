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

            # Load ADK agents from adk_agents/
            await self._load_adk_agent("greeting_agent")
            await self._load_adk_agent("news_pipeline")

            logger.info("Agent manager initialized successfully")
            logger.info(f"Loaded {len(self.agents)} ADK agents: {list(self.agents.keys())}")
        except Exception as e:
            logger.error(f"Failed to initialize agent manager: {str(e)}")
            raise

    async def _load_adk_agent(self, agent_name: str):
        """Load an ADK agent configuration from adk_agents/ directory"""
        try:
            # Read agent configuration directly from adk_agents/
            agent_dir = Path(__file__).parent.parent / "adk_agents" / agent_name
            agent_file = agent_dir / "agent.py"

            if not agent_file.exists():
                raise FileNotFoundError(f"Agent file not found: {agent_file}")

            # Extract agent configuration by reading the file
            # We'll parse the Agent definition to get model and instruction
            agent_config = self._parse_agent_config(agent_file)

            # Store simplified agent config (not the full ADK agent object)
            self.agents[agent_name] = agent_config
            logger.info(f"Loaded ADK agent config: {agent_name}")

        except Exception as e:
            logger.error(f"Failed to load agent {agent_name}: {str(e)}")
            raise

    def _parse_agent_config(self, agent_file: Path) -> Dict:
        """Parse ADK agent.py file to extract configuration"""
        # Read the agent file content
        content = agent_file.read_text()

        # Simple extraction (production would use AST parsing)
        config = {
            "model": "gemini-2.0-flash-exp",  # default
            "instruction": None
        }

        # Extract model
        if 'model="' in content:
            start = content.find('model="') + 7
            end = content.find('"', start)
            config["model"] = content[start:end]

        # Extract instruction
        if 'instruction="""' in content:
            start = content.find('instruction="""') + 15
            end = content.find('"""', start)
            config["instruction"] = content[start:end].strip()

        return config
    
    async def stream_chat(
        self,
        session_id: str,
        message: str,
        agent_name: str = "greeting_agent"
    ) -> AsyncGenerator[Dict, None]:
        """Stream chat responses from an ADK agent"""
        try:
            # Get the ADK agent configuration
            if agent_name not in self.agents:
                yield {"error": f"Agent '{agent_name}' not found. Available: {list(self.agents.keys())}"}
                return

            agent_config = self.agents[agent_name]

            # Get or create session history
            if session_id not in self.sessions:
                self.sessions[session_id] = []

            # Build the contents with system instruction from ADK agent
            contents = []

            # Add system instruction if available
            if agent_config.get("instruction"):
                # First message includes system instruction
                if len(self.sessions[session_id]) == 0:
                    contents.append({
                        "role": "user",
                        "parts": [{"text": f"{agent_config['instruction']}\n\nUser: {message}"}]
                    })
                else:
                    # For subsequent messages, use history + new message
                    contents = self.sessions[session_id].copy()
                    contents.append({
                        "role": "user",
                        "parts": [{"text": message}]
                    })
            else:
                # No instruction, just use message
                contents.append({
                    "role": "user",
                    "parts": [{"text": message}]
                })

            # Stream response using ADK agent's model configuration
            from google import genai
            client = genai.Client(api_key=settings.google_api_key)

            response = await client.aio.models.generate_content_stream(
                model=agent_config["model"],
                contents=contents
            )

            full_response = ""

            async for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    yield {
                        "type": "chunk",
                        "content": chunk.text,
                        "agent": agent_name
                    }

            # Add assistant response to history
            self.sessions[session_id].append({
                "role": "model",
                "parts": [{"text": full_response}]
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
