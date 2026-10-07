from pydantic import BaseModel
from typing import List, Optional, Any, Dict

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    steps: List[Dict[str, Any]] = []

class ToolResponse(BaseModel):
    name: str
    description: str
    schema_def: Dict[str, Any]

class HistoryResponse(BaseModel):
    messages: List[Dict[str, str]]
