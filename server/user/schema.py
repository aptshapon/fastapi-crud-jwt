from pydantic import BaseModel, EmailStr, Field, SecretStr


class User(BaseModel):
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

    class Config:
        orm_mode = True,
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
