from unittest.mock import MagicMock
import pytest

from dao.model.user import User
from dao.user_dao import UserDAO
from service.user_service import UserService
from setup_db import db

@pytest.fixture()
def user_dao():
    user_dao = UserDAO(db.session)

    andy = User(id=1, name='andy', surname='anderson', email='alan@gmail.com', password='qwerty', favorite_genre_id='1')
    bill = User(id=2, name='bill', surname='burton', email='bert@gmail.com', password='12345', favorite_genre_id='2')
    cary = User(id=3, name='carl', surname='carlson', email='cary@gmail.com', password='password', favorite_genre_id='3')

    user_dao.get_one_by_id = MagicMock(return_value=bill)
    user_dao.get_all = MagicMock(return_value=[andy, bill, cary])
    user_dao.create = MagicMock(return_value=User(id=4))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
    user_dao.change_password = MagicMock()

    return user_dao

class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one_by_id(self):
        user = self.user_service.get_one_by_id(2)
        assert user is not None
        assert user.id == 2

    def test_get_all(self):
        users = self.user_service.get_all()
        assert len(users) > 0

    def test_create(self):
        data = {'name': 'dany', 'surname': 'duffy', 'email': 'dany@gmail.com', 'password': 'dany', 'favorite_genre_id': '4'}
        user = self.user_service.create(data)
        assert user.id is not None

    def test_delete(self):
        self.user_service.delete(1)

    def test_update(self):
        data = {
            'id': 3,
            'name': 'carl'
        }
        self.user_service.update(data)

    def test_change_password(self):
        data = {'email': 'bert@gmail.com',
                'password_1': '12345',
                'password_2': '87tyrgh48h7'
            }
        self.user_service.change_password(data)

