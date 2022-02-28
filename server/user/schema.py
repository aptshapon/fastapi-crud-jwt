from pydantic import BaseModel, EmailStr, Field, SecretStr


class User(BaseModel):
    name: str | None = None
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "email@yotech.ltd",
            }
        }


class UserInDB(User):
    hashed_password: SecretStr = Field(...)


def user_response_model(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def user_error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
