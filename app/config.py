from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = ""
    max_iterations: int = 10
    model: str = "gpt-4-turbo"
    workspace_dir: str = "workspace"

    class Config:
        env_file = ".env"

settings = Settings()
