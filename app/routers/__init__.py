from fastapi import FastAPI

from app.routers.user_routers import user_router


def init_routes(app: FastAPI):
    app.include_router(user_router)
