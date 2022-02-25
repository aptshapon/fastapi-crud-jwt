from fastapi import Body, APIRouter
from fastapi.encoders import jsonable_encoder

from ..models.student import response_model, error_response_model
from ..models.user import UserSchema, UserLoginSchema, user_response_model
from ..auth.auth_handler import sign_jwt
from ..db.user import retrieve_users, add_user, delete_user

router = APIRouter()


@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return user_response_model(users, "Students data retrieved successfully")
    return user_response_model(users, "Empty list returned")


@router.post("/user/signup", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return [
        user_response_model(new_user, "User added successfully."),
        sign_jwt(user["email"])
    ]


@router.post("/user/login")
async def user_login(data: UserLoginSchema = Body(...)):
    user_data = jsonable_encoder(data)
    users = await retrieve_users()
    print("user_data----:", user_data)
    for user in users:
        if user["email"] == user_data["email"] and user["password"] == user_data["password"]:
            return sign_jwt(user["email"])
    return {
        "error": "Wrong login details!"
    }


@router.delete("/user/{id}", response_description="User data deleted from the database")
async def delete_user_data(delete_id: str):
    deleted_user = await delete_user(delete_id)
    if deleted_user:
        return response_model(
            f"Student with ID: {delete_id} removed", "User deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, f"User with id {delete_id} doesn't exist"
    )
