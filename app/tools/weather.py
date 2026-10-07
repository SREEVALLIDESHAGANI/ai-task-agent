from app.tools.registry import Tool, tool_registry

async def get_weather(location: str) -> str:
    # Mock implementation
    return f"The weather in {location} is currently 72°F and sunny."

weather_tool = Tool(
    name="weather",
    description="Get current weather information for a location.",
    parameters={
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g., 'San Francisco, CA'"
            }
        },
        "required": ["location"]
    },
    func=get_weather
)

tool_registry.register(weather_tool)
