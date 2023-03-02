from flask_restx import Resource, Namespace
from implemented import movie_schema, movies_schema, movie_service
from helpers.decorators import auth_required
from parsers import page_parser
movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        filters = page_parser.parse_args()
        movies = movie_service.get_all(filters)
        return movies_schema.dump(movies), 200

    # @admin_required
    # def post(self):
    #     data = request.json
    #     movie_service.create(data)
    #     return "Movie added", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one_by_id(mid)
        if movie is None:
            return 'Movie not found', 404
        return movie_schema.dump(movie), 200

    # @admin_required
    # def put(self, mid):
    #     data = request.json
    #     data['id'] = mid
    #     if movie_service.get_one_by_id(mid) is None:
    #         return 'Movie not found', 404
    #     movie_service.update(data)
    #     return "Movie updated", 201
    #
    # @admin_required
    # def delete(self, mid):
    #     if movie_service.get_one_by_id(mid) is None:
    #         return 'Movie not found', 404
    #     movie_service.delete(mid)
    #     return "Movie deleted", 201
