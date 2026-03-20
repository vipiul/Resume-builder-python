from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token
from app.models.user import User
from hashlib import sha256
from app.core.config import settings
from datetime import datetime, timedelta

class AuthService:
    @staticmethod
    async def register(email: str, password: str, full_name: str | None = None) -> User:
        hashed = hash_password(password)
        user = await UserRepository.create({
            "email": email,
            "hashed_password": hashed,
            "full_name": full_name
        })
        return user

    @staticmethod
    async def authenticate(email: str, password: str):
        user = await UserRepository.get_by_email(email)
        print("Authenticating user:", user)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        access = create_access_token(str(user.id))
        refresh = create_refresh_token(str(user.id))
        refresh_hash = sha256(refresh.encode()).hexdigest()
        await UserRepository.set_refresh_hash(user, refresh_hash)
        return {"access_token": access, "refresh_token": refresh}