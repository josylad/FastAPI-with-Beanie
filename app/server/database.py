from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from beanie import init_beanie

from app.server.models.product_review import ProductReview


MONGO_URL = config("MONGO_URL")


# Connect to MongoDB
async def init_db():
    if not MONGO_URL:
        raise ValueError("MONGO_URL environment variable is not set")

    client = AsyncIOMotorClient(MONGO_URL)

    if not client:
        raise Exception("Failed to connect to MongoDB")

    await init_beanie(database=client.students_fastapi, document_models=[ProductReview])

