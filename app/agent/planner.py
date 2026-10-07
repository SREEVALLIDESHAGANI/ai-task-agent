from typing import List

class Planner:
    def __init__(self):
        pass
        
    def decompose(self, task: str) -> List[str]:
        # A simple naive planner (could be LLM based)
        return [f"Step 1: Analyze {task}", "Step 2: Execute required tools"]
