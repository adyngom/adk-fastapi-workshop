"""
Main FastAPI application with Google ADK integration
"""
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import logging
from typing import Optional
import json

from api.routes import agents, health
from api.models.requests import ChatRequest, ChatResponse
from agents.manager import AgentManager
from config.settings import settings

# Configure logging
logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global agent manager
agent_manager: Optional[AgentManager] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    global agent_manager
    
    # Startup
    logger.info("Starting ADK FastAPI application...")
    agent_manager = AgentManager()
    await agent_manager.initialize()
    logger.info("Agent manager initialized")

    # Inject agent_manager into routes
    from api.routes import agents as agents_routes
    agents_routes.set_agent_manager(agent_manager)
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")
    if agent_manager:
        await agent_manager.cleanup()

# Create FastAPI app
app = FastAPI(
    title="Google ADK + FastAPI Workshop",
    description="Full-stack agentic AI application framework",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(agents.router, prefix="/api/agents", tags=["agents"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to the Google ADK + FastAPI Workshop API!",
        "docs": "/docs",
        "health": "/api/health"
    }

@app.websocket("/ws/chat/{session_id}")
async def websocket_chat(websocket: WebSocket, session_id: str):
    """WebSocket endpoint for real-time chat with agents"""
    await websocket.accept()
    logger.info(f"WebSocket connection established: {session_id}")
    
    try:
        while True:
            # Receive message
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Process with agent manager
            if agent_manager:
                async for chunk in agent_manager.stream_chat(
                    session_id=session_id,
                    message=message_data.get("message", ""),
                    agent_name=message_data.get("agent", "default")
                ):
                    await websocket.send_json(chunk)
            else:
                await websocket.send_json({
                    "error": "Agent manager not initialized"
                })
                
    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected: {session_id}")
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
        log_level=settings.log_level.lower()
    )
