from fastapi import FastAPI, Depends

from . import config
from server.student.route import router as student_router
from server.user.router import router as user_router
from server.auth.router import router as auth_router

app = FastAPI()

app.include_router(student_router, tags=["Student"], prefix="/student")
app.include_router(user_router, tags=["User"], prefix="/user")
app.include_router(auth_router, tags=["Auth"], prefix="/auth")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/info")
async def info(settings: config.Settings = Depends(config.get_settings)):
    return {
        "app_name": settings.app_name,
        "database": settings.db_name
    }
