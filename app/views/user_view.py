from fastapi import HTTPException

from app.schemas.user_schemas import (
    StandardOutput,
    UserCreateInput,
    UserFavoriteAddInput,
)
from app.services.favorite_service import FavoriteService
from app.services.user_services import UserService

user_service = UserService()
favorite_service = FavoriteService()


class UserView:
    @staticmethod
    async def user_create(data: UserCreateInput):
        try:
            await user_service.create(data)
            return StandardOutput(message="User created!")
        except Exception as error:
            raise HTTPException(400, detail=str(error))

    @staticmethod
    async def user_delete(id: int):
        try:
            await user_service.delete(id)
            return StandardOutput(message="User deleted!")
        except Exception as error:
            raise HTTPException(400, detail=str(error))

    @staticmethod
    async def list_user():
        try:
            return await user_service.find_all()
        except Exception as error:
            raise HTTPException(400, detail=str(error))

    @staticmethod
    async def add_favorite(data: UserFavoriteAddInput):
        try:
            await favorite_service.create(data)
            return StandardOutput(message="Favorite added!")
        except Exception as error:
            raise HTTPException(400, detail=str(error))

    @staticmethod
    async def remove_favorite(id: int):
        try:
            await favorite_service.delete(id)
            return StandardOutput(message="Favorite removed!")
        except Exception as error:
            raise HTTPException(400, detail=str(error))
