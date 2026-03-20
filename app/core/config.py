from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    mongodb_uri: str = Field("mongodb://localhost:27017/myapp", env="MONGODB_URI")
    jwt_secret: str = Field(..., env="JWT_SECRET")
    jwt_algo: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30

    class Config:
        env_file = ".env"

settings = Settings()