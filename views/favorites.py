from flask import request
from flask_restx import Resource, Namespace
from implemented import favorites_schema, favorite_service
from helpers.decorators import auth_required
from parsers import page_parser

favorite_ns = Namespace('favorites/movies')


@favorite_ns.route('/')
class FavoritesView(Resource):
    @auth_required
    def get(self):
        filters = page_parser.parse_args()
        favorites = favorite_service.get_all(filters)
        return favorites_schema.dump(favorites), 200


@favorite_ns.route('/<int:mid>')
class FavoriteView(Resource):

    @auth_required
    def post(self, mid):
        data = request.json
        data['movie_id'] = mid
        if favorite_service.get_one_by_user_and_movie(data) is not None:
            return 'Movie is already in favorites'
        favorite_service.add(data)
        return "Movie added to favorites", 201

    @auth_required
    def delete(self, mid):
        data = request.json
        data['movie_id'] = mid
        favorite_service.delete(data)
        return "Movie removed from favorites", 201
