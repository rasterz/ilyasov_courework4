from dao.movie_dao import MovieDAO
from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.user_dao import UserDAO
from dao.favorite_dao import FavoriteDAO

from service.movie_service import MovieService
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.user_service import UserService
from service.auth_service import AuthService
from service.favorite_service import FavoriteService


from dao.model.movie import MovieSchema
from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema
from dao.model.user import UserSchema
from dao.model.favorite import FavoriteSchema


from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

user_dao = UserDAO(db.session)
user_service = UserService(dao=user_dao)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

auth_service = AuthService(user_service)

favorite_dao = FavoriteDAO(db.session)
favorite_service = FavoriteService(dao=favorite_dao)
favorites_schema = FavoriteSchema(many=True)

