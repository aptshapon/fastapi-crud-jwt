from motor.motor_asyncio import AsyncIOMotorClient
from server.config import settings

client = AsyncIOMotorClient(settings.DB_URL)
database = client[settings.DB_NAME]
student_collection = database.get_collection("students_collection")
user_collection = database.get_collection("users_collection")
