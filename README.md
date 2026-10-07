# AI Task Agent — Tool-Calling LLM Assistant

An LLM-powered AI agent capable of understanding natural-language tasks, planning execution steps, and selecting appropriate tools to complete multi-step workflows.

## Features
- **LLM-Powered Agent**: Understands complex tasks and executes them.
- **OpenAI Function Calling**: Structured interaction with external utilities.
- **Agent Loop**: Planning, Tool Selection, Execution, Observation, Response.
- **Short-Term Memory**: Conversation memory to maintain context.
- **Tool Ecosystem**: Includes tools for calculation, web search, file management, code execution, and weather.

## Architecture

```
User -> FastAPI Backend -> Agent Loop
                              | -> Planner (Decomposes task)
                              | -> Selector (Chooses tool)
                              | -> Executor (Runs tool via OpenAI tools schema)
                              | -> Memory (Stores context)
```

## Tech Stack
- Python 3.10+
- OpenAI API
- FastAPI
- Pydantic

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Add your OPENAI_API_KEY to .env
   ```
4. Run the server:
   ```bash
   python main.py
   ```

## Usage

Send a message to the agent:
```bash
curl -X POST "http://localhost:8000/api/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "What is the weather in Tokyo and then calculate 5 + 5?"}'
```

## Adding Custom Tools
Implement a new tool in `app/tools/` using the Tool schema in `app/tools/registry.py` and register it in the registry.

## Screenshots
*(Placeholder for screenshots)*
