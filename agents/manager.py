"""
Agent Manager for coordinating multiple ADK agents
"""
import logging
from typing import Dict, List, Optional, AsyncGenerator
from google import genai
from google.genai import types
from config.settings import settings

logger = logging.getLogger(__name__)

class AgentManager:
    """Manages multiple ADK agents and their interactions"""
    
    def __init__(self):
        self.agents: Dict[str, any] = {}
        self.client: Optional[genai.Client] = None
        self.sessions: Dict[str, any] = {} # In-memory session store
        
    async def initialize(self):
        """Initialize the agent manager and create agents"""
        try:
            # Configure Gemini client with API key
            self.client = genai.Client(api_key=settings.google_api_key)

            # Create default agent
            await self._create_default_agent()

            logger.info("Agent manager initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize agent manager: {str(e)}")
            raise
    
    async def _create_default_agent(self):
        """Create a default general-purpose agent"""
        # This is a placeholder - implement with actual ADK agent creation
        self.agents["default"] = {
            "name": "default",
            "description": "General purpose assistant",
            "model": settings.default_model
        }
    
    async def stream_chat(
        self, 
        session_id: str, 
        message: str, 
        agent_name: str = "default"
    ) -> AsyncGenerator[Dict, None]:
        """Stream chat responses from an agent"""
        try:
            if agent_name not in self.agents:
                yield {"error": f"Agent '{agent_name}' not found"}
                return

            if not self.client:
                 yield {"error": "Gemini client not initialized"}
                 return
            
            # Get or create session
            if session_id not in self.sessions:
                self.sessions[session_id] = []
            
            # Add user message to history
            self.sessions[session_id].append({
                "role": "user",
                "parts": [{"text": message}]
            })
            
            # Stream response from model
            response = await self.client.aio.models.generate_content_stream(
                model=self.agents[agent_name]["model"],
                contents=self.sessions[session_id]
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
