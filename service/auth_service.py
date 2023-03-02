import datetime
import calendar
import jwt
from flask import abort

from service.user_service import UserService
from helpers.constants import SECRET, ALGO

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_one_by_email(email)

        if user is None:
            abort(400)
        if not is_refresh:
            if not self.user_service.check_password(user.password, password):
                abort(400)

        data = {'email': email}

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data['exp'] = calendar.timegm(days30.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def refresh_token(self, token):
        data = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])
        email = data.get('email')

        return self.generate_token(email, None, is_refresh=True)

    def register_user(self, user_d):
        return self.user_service.create(user_d)

