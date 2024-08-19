from django.db.models.base import Model as Model

from ....utils.helpers.orm import BaseRepository
from ..models import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
