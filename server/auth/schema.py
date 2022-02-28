from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


def user_response_model(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message}


def user_error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
