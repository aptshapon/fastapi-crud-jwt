import motor.motor_asyncio
from decouple import config


MONGO_DETAILS = config("db_url")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students_collection")
user_collection = database.get_collection("users_collection")
