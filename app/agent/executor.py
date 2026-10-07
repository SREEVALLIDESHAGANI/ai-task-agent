from typing import Any, Dict
from app.tools.registry import ToolRegistry

class ToolExecutor:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    async def execute(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        tool = self.registry.get_tool(tool_name)
        if not tool:
            raise ValueError(f"Tool {tool_name} not found")
        
        return await tool.run(**arguments)
