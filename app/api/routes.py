from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import ChatRequest, ChatResponse, ToolResponse, HistoryResponse
from app.agent.agent import Agent
from app.agent.memory import ConversationMemory
from app.tools.registry import tool_registry

router = APIRouter()
memory = ConversationMemory()
agent = Agent(memory=memory, registry=tool_registry)

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response, steps = await agent.run(request.message)
        return ChatResponse(response=response, steps=steps)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tools", response_model=List[ToolResponse])
def get_tools():
    tools = []
    for name, tool in tool_registry.tools.items():
        tools.append(ToolResponse(
            name=name,
            description=tool.description,
            schema_def=tool.parameters
        ))
    return tools

@router.get("/history", response_model=HistoryResponse)
def get_history():
    return HistoryResponse(messages=memory.get_messages())

@router.delete("/history")
def clear_history():
    memory.clear()
    return {"status": "success", "message": "History cleared"}
