from unittest.mock import MagicMock
import pytest

from dao.model.director import Director
from dao.director_dao import DirectorDAO
from service.director_service import DirectorService
from setup_db import db

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    alan = Director(id=1, name='alan')
    bert = Director(id=2, name='bert')
    carl = Director(id=3, name='carl')

    director_dao.get_one_by_id = MagicMock(return_value=alan)
    director_dao.get_all = MagicMock(return_value=[alan, bert, carl])

    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one_by_id(self):
        director = self.director_service.get_one_by_id(1)
        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        filters = []
        directors = self.director_service.get_all(filters)
        assert len(directors) > 0
