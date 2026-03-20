from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.user import User

mongo_client: AsyncIOMotorClient | None = None

async def init_db():
    global mongo_client
    mongo_client = AsyncIOMotorClient(settings.mongodb_uri)
    await init_beanie(database=mongo_client.get_default_database(), document_models=[User])