from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie_dao import MovieDAO
from service.movie_service import MovieService
from setup_db import db

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    saw_1 = Movie(id=1, title='saw_1', description='desc_1', trailer='trl_1', year=2004, rating=3, genre_id=1, director_id=1)
    saw_2 = Movie(id=2, title='saw_2', description='desc_2', trailer='trl_2', year=2005, rating=3, genre_id=1, director_id=1)
    saw_3 = Movie(id=3, title='saw_3', description='desc_3', trailer='trl_3', year=2006, rating=3, genre_id=1, director_id=1)

    movie_dao.get_one_by_id = MagicMock(return_value=saw_1)
    movie_dao.get_all = MagicMock(return_value=[saw_1, saw_2, saw_3])

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one_by_id(self):
        movie = self.movie_service.get_one_by_id(1)
        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        filters = []
        movies = self.movie_service.get_all(filters)
        assert len(movies) > 0
