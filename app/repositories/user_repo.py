from app.models.user import User
from typing import Optional


class UserRepository:
    @staticmethod
    async def get_by_email(email: str) -> Optional[User]:
        return await User.find_one(User.email == email)

    @staticmethod
    async def create(user_data: dict) -> User:
        user = User(**user_data)
        await user.insert()
        return user

    @staticmethod
    async def set_refresh_hash(user: User, refresh_hash: str):
        user.refresh_token_hash = refresh_hash
        await user.save()