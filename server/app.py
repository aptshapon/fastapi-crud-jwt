from fastapi import FastAPI, Depends

from . import config
from .config import get_settings
from .routes.student import router as student_router
from .routes.user import router as user_router

app = FastAPI()

app.include_router(student_router, tags=["Student"], prefix="/student")
app.include_router(user_router, tags=["User"], prefix="/user")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/info")
async def info(settings: config.Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "database": settings.db_name
    }
