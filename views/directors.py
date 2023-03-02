from flask import request
from flask_restx import Resource, Namespace
from implemented import director_schema, directors_schema, director_service
from helpers.decorators import auth_required
from parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        filters = page_parser.parse_args()
        directors = director_service.get_all(filters)
        return directors_schema.dump(directors), 200

    # @admin_required
    # def post(self):
    #     data = request.json
    #     director_service.create(data)
    #     return "Director added", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one_by_id(did)
        if director is None:
            return 'Director not found', 404
        return director_schema.dump(director), 200

    # @admin_required
    # def put(self, did):
    #     data = request.json
    #     data['id'] = did
    #     if director_service.get_one_by_id(did) is None:
    #         return 'Director not found', 404
    #     director_service.update(data)
    #     return "Director updated", 201
    #
    # @admin_required
    # def delete(self, did):
    #     if director_service.get_one_by_id(did) is None:
    #         return 'Director not found', 404
    #     director_service.delete(did)
    #     return "Director deleted", 201
