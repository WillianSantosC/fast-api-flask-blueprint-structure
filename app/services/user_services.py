from .crud_service import CrudService
from app.database.models import User


class UserService(CrudService):
    def __init__(self) -> None:
        super().__init__(User)
