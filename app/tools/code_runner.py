import sys
from io import StringIO
from app.tools.registry import Tool, tool_registry

async def run_code(code: str) -> str:
    # A restricted code runner, outputs only what is printed
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        # Avoid running dangerous imports
        if "import os" in code or "import sys" in code or "import subprocess" in code:
            return "Execution rejected: unsafe imports detected."
            
        exec(code, {"__builtins__": __builtins__})
    except Exception as e:
        sys.stdout = old_stdout
        return f"Error executing code: {str(e)}"
        
    sys.stdout = old_stdout
    return redirected_output.getvalue()

code_runner_tool = Tool(
    name="code_runner",
    description="Execute Python code snippets securely and return standard output. Do not use for file ops or sys/os modules.",
    parameters={
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The Python code to execute"
            }
        },
        "required": ["code"]
    },
    func=run_code
)

tool_registry.register(code_runner_tool)
