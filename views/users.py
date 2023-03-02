from flask import request
from flask_restx import Resource, Namespace
from helpers.decorators import auth_required
from dao.model.user import UserSchema
from implemented import user_service
from helpers.exceptions import PasswordWrong

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        data = user_service.get_all()
        return UserSchema(many=True).dump(data), 200

    @auth_required
    def post(self):
        data = request.json
        user_service.create(data)
        return "User added", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):

    @auth_required
    def get(self, uid):
        user = user_service.get_one_by_id(uid)
        if user is None:
            return 'User not found', 404
        return UserSchema().dump(user), 200

    @auth_required
    def patch(self, uid):
        data = request.json
        data['id'] = uid
        if user_service.get_one_by_id(uid) is None:
            return 'User not found', 404
        user_service.update(data)
        return "User updated", 201

    @auth_required
    def delete(self, uid):
        if user_service.get_one_by_id(uid) is None:
            return 'User not found', 404
        user_service.delete(uid)
        return "User deleted", 201

@user_ns.route('/<int:uid>/password')
class UserPassword(Resource):
    def patch(self, uid):
        data = request.json
        data['id'] = uid
        user = user_service.get_one_by_id(uid)
        if user is None:
            return 'User not found', 404
        try:
            user_service.check_password(user.password, data['password_1'])
        except PasswordWrong as error:
            return error.message, 401
        user_service.change_password(data)
        return "User updated", 201