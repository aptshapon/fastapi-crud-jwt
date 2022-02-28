from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .schema import Token

from ..user import hashing
from ..user.schema import User, UserInDB
from . import jwt

router = APIRouter()


def get_user(db, email: str):
    if email in db:
        user_dict = db[email]
        return UserInDB(**user_dict)


def authenticate_user(data, email: str, password: str):
    user = get_user(data, email)
    print("user:--------:", user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    if not hashing.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        users_db: dict = Depends(get_user)):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/", response_model=User)
async def read_users_me(current_user: User = Depends(jwt.get_current_user)):
    return current_user
