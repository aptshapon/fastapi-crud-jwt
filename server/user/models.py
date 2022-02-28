from bson import ObjectId
from fastapi import APIRouter
from server.db.db import user_collection
from server.user.hashing import get_password_hash

router = APIRouter()


# helpers
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }


# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one({
        "name": user_data["name"],
        "email": user_data["email"],
        "password": get_password_hash(user_data["password"])
    })
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Delete a student from the database
async def delete_user(user_id: str):
    student = await user_collection.find_one({"_id": ObjectId(user_id)})
    if student:
        await user_collection.delete_one({"_id": ObjectId(user_id)})
        return True
