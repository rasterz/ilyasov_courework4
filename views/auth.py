from flask import request, abort
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        data = request.json
        auth_service.register_user(data)
        return "User added", 201

@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self):
        data = request.json

        email = data.get('email')
        password = data.get('password')

        if None in [email, password]:
            abort(401)

        tokens = auth_service.generate_token(email, password)
        return tokens, 200

    def put(self):
        data = request.json
        token = data.get('refresh_token')

        if token is None:
            abort(401)

        tokens = auth_service.refresh_token(token)
        return tokens, 200