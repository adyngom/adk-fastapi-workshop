"""Agent management endpoints"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from api.models.requests import ChatRequest, ChatResponse
from api.models.agent import AgentInfo
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/list", response_model=List[AgentInfo])
async def list_agents():
    """List all available agents"""
    # TODO: Implementation will use agent_manager
    return [
        AgentInfo(
            name="default",
            description="General purpose assistant agent",
            capabilities=["chat", "search","analysis"]
        )
    ]

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
