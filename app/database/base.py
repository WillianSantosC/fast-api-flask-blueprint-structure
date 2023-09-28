# Import all the models, so that Base has them before being
# imported by Alembic

from app.database.connection import Base
from app.models.favorites_model import Favorite
from app.models.user_model import User
