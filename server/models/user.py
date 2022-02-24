from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Shapon Sheikh",
                "email": "shapon@yotech.ltd",
                "password": "Aa112233"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "shapon@yotech.ltd",
                "password": "Aa112233"
            }
        }


def user_response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def user_error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
