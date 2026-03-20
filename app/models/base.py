from beanie import Document
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Base(Document):
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime]


class Settings:
    use_state_management = True