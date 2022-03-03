from pydantic import BaseModel, EmailStr, Field, SecretStr, constr


class User(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        orm_mode = True,
        schema_extra = {
            "example": {
                "name": "Shapon Sheikh",
                "email": "shapon@yotech.ltd",
                "password": "password",
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
