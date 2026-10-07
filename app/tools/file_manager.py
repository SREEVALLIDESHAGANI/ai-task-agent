import os
from app.tools.registry import Tool, tool_registry
from app.config import settings

os.makedirs(settings.workspace_dir, exist_ok=True)

async def manage_file(action: str, filename: str, content: str = "") -> str:
    filepath = os.path.join(settings.workspace_dir, filename)
    
    if action == "read":
        if not os.path.exists(filepath):
            return "File not found."
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
            
    elif action == "write":
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return "File written successfully."
        
    elif action == "list":
        return ", ".join(os.listdir(settings.workspace_dir))
        
    return "Invalid action."

file_manager_tool = Tool(
    name="file_manager",
    description="Read, write, or list files in the sandbox workspace directory.",
    parameters={
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["read", "write", "list"],
                "description": "The action to perform"
            },
            "filename": {
                "type": "string",
                "description": "The name of the file (for read/write)"
            },
            "content": {
                "type": "string",
                "description": "The content to write (only for 'write' action)"
            }
        },
        "required": ["action"]
    },
    func=manage_file
)

tool_registry.register(file_manager_tool)
