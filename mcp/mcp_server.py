"""
Stub MCP Server for workshop demonstration
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

app = FastAPI(
    title="ADK Workshop - Stub MCP Server",
    description="Provides MCP-compatible tool definitions"
)

# Example tools
MCP_TOOLS = [
    {
        "name": "file_reader",
        "description": "Read and analyze files from a specific directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Path to the file"}
            },
            "required": ["file_path"]
        }
    },
    {
        "name": "database_query",
        "description": "Query the workshop database",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "SQL query to execute"},
                "database": {"type": "string", "description": "Database name"}
            },
            "required": ["query"]
        }
    }
]

@app.get("/.well-known/mcp/tools")
async def discover_tools():
    """MCP standard discovery endpoint"""
    return {"tools": MCP_TOOLS}

class ToolCallRequest(BaseModel):
    parameters: Dict[str, Any]

@app.post("/tools/{tool_name}/call")
async def call_tool(tool_name: str, request: ToolCallRequest):
    """MCP standard tool call endpoint"""
    if tool_name not in [tool["name"] for tool in MCP_TOOLS]:
        raise HTTPException(status_code=404, detail="Tool not found")
    
    # Placeholder: Just echo parameters
    return {
        "status": "success",
        "result": {
            "message": f"Tool '{tool_name}' called with parameters",
            "params_received": request.parameters
        }
    }

@app.get("/")
async def root():
    return {"message": "MCP Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
