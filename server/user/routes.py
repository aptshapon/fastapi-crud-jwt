from fastapi import Body, APIRouter, status
from fastapi.encoders import jsonable_encoder

from server.auth.token import create_access_token
from server.student.student import response_model, error_response_model
from server.user.schema import User, user_response_model
from server.user.models import retrieve_users, add_user, delete_user

router = APIRouter()


@router.get("/", response_description="Users retrieved",
            status_code=status.HTTP_200_OK)
async def get_users():
    users = await retrieve_users()
    if users:
        return user_response_model(users, "Users data retrieved successfully")
    return user_response_model(users, "Empty list returned")


@router.post("/", response_description="User data added into the database",
             status_code=status.HTTP_201_CREATED)
async def add_user_data(user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return [
        user_response_model(new_user, "User added successfully."),
        create_access_token(user["email"])
    ]


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(delete_id: str):
    deleted_user = await delete_user(delete_id)
    if deleted_user:
        return response_model(
            f"User with ID: {delete_id} removed", "User deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, f"User with id {delete_id} doesn't exist"
    )
