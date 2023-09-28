from app.models.user_model import User

from .crud_service import CrudService


class UserService(CrudService):
    def __init__(self) -> None:
        super().__init__(User)
