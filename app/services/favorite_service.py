from .crud_service import CrudService
from app.database.models import Favorite


class FavoriteService(CrudService):
    def __init__(self) -> None:
        super().__init__(Favorite)
