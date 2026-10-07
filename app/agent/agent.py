from typing import List, Dict, Any, Tuple
import json
from openai import AsyncOpenAI
from app.config import settings
from app.agent.memory import ConversationMemory
from app.agent.executor import ToolExecutor
from app.agent.planner import Planner
from app.tools.registry import ToolRegistry
from app.agent.prompts import SYSTEM_PROMPT

class Agent:
    def __init__(self, memory: ConversationMemory, registry: ToolRegistry):
        self.memory = memory
        self.registry = registry
        self.executor = ToolExecutor(registry)
        self.planner = Planner()
        # Ensure API key is present or set to a dummy to avoid instantiation error if env is missing
        api_key = settings.openai_api_key or "dummy_key"
        self.client = AsyncOpenAI(api_key=api_key)

    async def run(self, user_message: str) -> Tuple[str, List[Dict[str, Any]]]:
        self.memory.add_user_message(user_message)
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + self.memory.get_messages()
        tools = self.registry.get_openai_tools()
        steps = []
        
        for _ in range(settings.max_iterations):
            # This is the selection phase
            response = await self.client.chat.completions.create(
                model=settings.model,
                messages=messages,
                tools=tools if tools else None,
                tool_choice="auto" if tools else None
            )
            
            choice = response.choices[0]
            message = choice.message
            
            if message.content:
                steps.append({"action": "think", "content": message.content})
            
            if message.tool_calls:
                # Observation / Execution phase
                messages.append(message) # add assistant tool call msg
                for tool_call in message.tool_calls:
                    function_name = tool_call.function.name
                    arguments = json.loads(tool_call.function.arguments)
                    
                    steps.append({"action": "execute", "tool": function_name, "args": arguments})
                    
                    try:
                        result = await self.executor.execute(function_name, arguments)
                    except Exception as e:
                        result = f"Error: {str(e)}"
                    
                    steps.append({"action": "observe", "result": result})
                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": str(result)
                    })
            else:
                # Final response phase
                final_response = message.content or ""
                self.memory.add_assistant_message(final_response)
                return final_response, steps
        
        final_response = "Max iterations reached without completion."
        self.memory.add_assistant_message(final_response)
        return final_response, steps
