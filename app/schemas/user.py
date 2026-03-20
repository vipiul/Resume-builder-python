from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str]


class UserRead(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str]
    roles: List[str]
    is_active: bool


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str
    exp: int