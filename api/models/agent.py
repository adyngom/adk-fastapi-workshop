"""Agent information models"""
from pydantic import BaseModel, Field
from typing import List, Optional

class AgentInfo(BaseModel):
    """Agent information"""
    name: str = Field(..., description="Agent name")
    description: str = Field(..., description="Agent description")
    capabilities: List[str] = Field(default_factory=list, description="Agent capabilities")
    status: str = Field(default="active", description="Agent status")
