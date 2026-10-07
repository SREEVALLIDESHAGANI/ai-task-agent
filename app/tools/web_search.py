from app.tools.registry import Tool, tool_registry

async def web_search(query: str) -> str:
    # Mock implementation
    return f"Search results for '{query}': 1. Example domain (example.com). 2. Wikipedia article about {query}."

web_search_tool = Tool(
    name="web_search",
    description="Simulate a web search to find information online.",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query"
            }
        },
        "required": ["query"]
    },
    func=web_search
)

tool_registry.register(web_search_tool)
