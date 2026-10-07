from app.tools.registry import Tool, tool_registry
import ast
import operator

def safe_eval(expr: str):
    # Very restricted math evaluator
    allowed_operators = {
        ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg
    }
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return allowed_operators[type(node.op)](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.UnaryOp):
            return allowed_operators[type(node.op)](eval_node(node.operand))
        else:
            raise TypeError(node)
    
    return eval_node(ast.parse(expr, mode='eval').body)

async def calculate(expression: str) -> str:
    try:
        result = safe_eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

calculator_tool = Tool(
    name="calculator",
    description="Evaluate mathematical expressions securely. Use operators like +, -, *, /, **",
    parameters={
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The math expression to evaluate, e.g. '2 + 2'"
            }
        },
        "required": ["expression"]
    },
    func=calculate
)

tool_registry.register(calculator_tool)
