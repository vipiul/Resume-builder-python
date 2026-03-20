from beanie import Document, Indexed
from pydantic import EmailStr, Field
from typing import List, Optional
from datetime import datetime

class User(Document):
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    refresh_token_hash: Optional[str] = None
    roles: List[str] = ["user"]
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
        indexes = ["email"]
