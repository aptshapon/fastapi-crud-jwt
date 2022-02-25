import uvicorn

from server.config import settings

if __name__ == "__main__":
    # uvicorn.run("server.app:app", host="127.0.0.1", port=8000, reload=True)

    uvicorn.run(
        "server.app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE
    )