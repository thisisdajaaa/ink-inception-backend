from django.db.models.base import Model as Model
from injector import inject

from ....utils.helpers.orm import BaseRepository
from ..models import Blog


class BlogRepository(BaseRepository):
    @inject
    def __init__(self, model: Blog):
        super().__init__(model)
