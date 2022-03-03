from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from . import token, schema
from ..database.db import user_collection
from ..user import hashing
from ..user.schema import User
from . import oauth2

router = APIRouter()


@router.post("/login", response_model=schema.Token)
async def login_for_access_token(request: OAuth2PasswordRequestForm = Depends()):
    user = await user_collection.find_one({"email": request.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    if not hashing.verify_password(request.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    # Generate a JWT token
    access_token = token.create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(oauth2.get_current_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: User = Depends(oauth2.get_current_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]
