import motor.motor_asyncio
from ..config import settings

MONGO_DATABASE_URL = f"mongodb://{settings.MGDB_USERNAME}:{settings.MGDB_PASSWORD}@{settings.MGDB_HOSTNAME}:{settings.MGDB_PORT}/{settings.MGDB_DBNAME}"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DATABASE_URL)