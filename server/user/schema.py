from pydantic import BaseModel, EmailStr, Field, SecretStr, constr


class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: SecretStr

    class Config:
        orm_mode = True,
        schema_extra = {
            "example": {
                "name": "Shapon Sheikh",
                "email": "shapon@yotech.ltd",
                "password": "password"
            }
        }



# class DisplayUser(BaseModel):
#     id: int
#     name: str
#     email: str
#
#     class Config:
#         orm_mode = True


def user_response_model(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def user_error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
