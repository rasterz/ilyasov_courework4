from unittest.mock import MagicMock
import pytest

from dao.model.genre import Genre
from dao.genre_dao import GenreDAO
from service.genre_service import GenreService
from setup_db import db

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    action = Genre(id=1, name='action')
    drama = Genre(id=2, name='drama')
    comedy = Genre(id=3, name='comedy')

    genre_dao.get_one_by_id = MagicMock(return_value=action)
    genre_dao.get_all = MagicMock(return_value=[action, drama, comedy])

    return genre_dao

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one_by_id(self):
        genre = self.genre_service.get_one_by_id(1)
        assert genre is not None
        assert genre.id == 1

    def test_get_all(self):
        filters = []
        genres = self.genre_service.get_all(filters)
        assert len(genres) > 0
