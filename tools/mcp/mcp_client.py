"""
Model Context Protocol (MCP) integration for ADK
Enables standardized tool communication across frameworks
"""
import logging
from typing import Dict, List, Optional
import httpx
from config.settings import settings

logger = logging.getLogger(__name__)

class MCPClient:
    """Client for interacting with MCP servers"""
    
    def __init__(self):
        self.server_url = settings.mcp_server_url
        self.available_tools: Dict[str, dict] = {}
        self.client = httpx.AsyncClient(base_url=self.server_url)
    
    async def discover_tools(self) -> List[Dict]:
        """Discover available tools from MCP server"""
        try:
            response = await self.client.get("/.well-known/mcp/tools")
            response.raise_for_status()
            tools = response.json().get("tools", [])
            self.available_tools = {tool["name"]: tool for tool in tools}
            logger.info(f"Discovered {len(tools)} tools from MCP server")
            return tools
        except Exception as e:
            logger.error(f"Failed to discover MCP tools: {e}")
            return []
    
    async def call_tool(self, tool_name: str, parameters: Dict) -> Dict:
        """Call a tool via MCP protocol"""
        logger.info(f"Calling MCP tool: {tool_name}")
        try:
            response = await self.client.post(
                f"/tools/{tool_name}/call",
                json={"parameters": parameters}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to call MCP tool {tool_name}: {e}")
            return {"error": str(e)}

