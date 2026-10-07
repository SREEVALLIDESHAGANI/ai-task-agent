import uvicorn
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Task Agent API", description="Tool-Calling LLM Assistant")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to AI Task Agent API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
