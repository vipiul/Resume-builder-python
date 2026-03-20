from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, Token
from app.services.auth_service import AuthService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=201)
async def register(payload: UserCreate):
    user = await AuthService.register(payload.email, payload.password, payload.full_name)
    return {"id": str(user.id), "email": user.email}


@router.post("/login", response_model=Token)
async def login(payload: UserCreate):
    tokens = await AuthService.authenticate(payload.email, payload.password)
    print("Login attempt for:", payload, tokens)
    if not tokens:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": tokens["access_token"], "token_type": "bearer"}