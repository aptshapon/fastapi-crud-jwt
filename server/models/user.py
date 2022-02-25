from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserSchema(BaseModel):
    name: str = Field(...)
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "username": "username",
                "email": "email@yotech.ltd",
                "password": "password"
            }
        }


class UserLoginSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: SecretStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "username",
                "email": "email@yotech.ltd",
                "password": "password"
            }
        }


def user_response_model(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def user_error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
