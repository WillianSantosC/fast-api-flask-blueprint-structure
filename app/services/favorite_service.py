from app.models.favorites_model import Favorite

from .crud_service import CrudService


class FavoriteService(CrudService):
    def __init__(self) -> None:
        super().__init__(Favorite)
