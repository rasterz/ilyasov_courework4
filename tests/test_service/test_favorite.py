from unittest.mock import MagicMock
import pytest

from dao.model.favorite import Favorite
from dao.favorite_dao import FavoriteDAO
from service.favorite_service import FavoriteService
from setup_db import db

@pytest.fixture()
def favorite_dao():
    favorite_dao = FavoriteDAO(db.session)

    favorite_1 = Favorite(id=1, user_id='1', movie_id='2')
    favorite_2 = Favorite(id=2, user_id='4', movie_id='2')
    favorite_3 = Favorite(id=3, user_id='1', movie_id='3')
    
    favorite_dao.get_all = MagicMock(return_value=[favorite_1, favorite_2, favorite_3])
    favorite_dao.get_one_by_user_and_movie = MagicMock(return_value=favorite_3)
    favorite_dao.add = MagicMock(return_value=Favorite(id=4))
    favorite_dao.delete = MagicMock()


    return favorite_dao

class TestFavoriteService:
    @pytest.fixture(autouse=True)
    def favorite_service(self, favorite_dao):
        self.favorite_service = FavoriteService(dao=favorite_dao)

    def test_get_one_by_id(self):
        data = {'user_id': 1, 'movie_id': 3}
        favorite = self.favorite_service.get_one_by_user_and_movie(data)
        assert favorite is not None
        assert favorite.id == 3

    def test_get_all(self):
        filters=[]
        favorites = self.favorite_service.get_all(filters)
        assert len(favorites) > 0

    def test_add(self):
        data = {'user_id': 4, 'movie_id': 5}
        favorite = self.favorite_service.add(data)
        assert favorite.id is not None

    def test_delete(self):
        self.favorite_service.delete(1)
