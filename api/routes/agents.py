"""Agent management endpoints"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from api.models.requests import ChatRequest, ChatResponse
from api.models.agent import AgentInfo
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# Will be injected by main.py
_agent_manager = None

def set_agent_manager(manager):
    """Set the global agent manager (called from main.py)"""
    global _agent_manager
    _agent_manager = manager

@router.get("/list", response_model=List[AgentInfo])
async def list_agents():
    """List all available agents discovered from adk_agents/ directory"""
    if not _agent_manager:
        raise HTTPException(status_code=503, detail="Agent manager not initialized")

    try:
        agent_infos = []
        for agent_name, agent_obj in _agent_manager.agents.items():
            # Extract metadata from ADK agent object
            info = AgentInfo(
                name=agent_name,
                description=getattr(agent_obj, 'description', f"ADK agent: {agent_name}"),
                capabilities=["chat", "streaming", "tools"] if hasattr(agent_obj, 'tools') and agent_obj.tools else ["chat", "streaming"],
                status="active"
            )
            agent_infos.append(info)

        return agent_infos
    except Exception as e:
        logger.error(f"Error listing agents: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    """Send a message to an agent and get response"""
    try:
        # TODO: Implementation will use agent_manager
        return ChatResponse(
            message="This is a non-streamed response from the agent.",
            agent=request.agent or "default",
            session_id=request.session_id or "session-id-http"
        )
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
