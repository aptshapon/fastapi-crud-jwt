from motor.motor_asyncio import AsyncIOMotorClient
from server.config import settings

client = AsyncIOMotorClient(settings.db_url)
database = client[settings.db_name]
student_collection = database.get_collection("students_collection")
user_collection = database.get_collection("users_collection")
