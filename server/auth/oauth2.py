from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
<<<<<<< HEAD

from server.auth import token

=======
from jose import jwt, JWTError

from server.auth import token
from server.auth.token import SECRET_KEY, ALGORITHM
from server.auth.schema import TokenData
from server.user import hashing, models
from server.user.schema import User
>>>>>>> 9aa1e4d... fixed bugs most of the token, oauth login

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    return token.verify_token(data, credentials_exception)
<<<<<<< HEAD
=======

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


def get_user(db, email: str):
    print("database::", db)
    if email in db:
        user_dict = db["email"]
        return User(**user_dict)


def authenticate_user(db, email: str, password: str):
    user = get_user(db, email)
    user = database.query(User).filter(User.email == request.username).first()
    user = db["users"].find_one({"username":request.username})

    print(user, email, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not hashing.verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    return user
>>>>>>> 9aa1e4d... fixed bugs most of the token, oauth login
