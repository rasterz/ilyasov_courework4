import jwt
from helpers.constants import ALGO, SECRET
from flask import request, abort

def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, key=SECRET, algorithms=[ALGO])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper

# def admin_required(func):
#     def wrapper(*args, **kwargs):
#         if 'Authorization' not in request.headers:
#             abort(401)
#
#         data = request.headers['Authorization']
#         token = data.split('Bearer ')[-1]
#         try:
#             user = jwt.decode(token, key=SECRET, algorithms=[ALGO])
#             if user['role'] != 'admin':
#                 return 'Role "admin" required', 403
#         except Exception as e:
#             print('JWT Decode Exception', e)
#             abort(401)
#         return func(*args, **kwargs)
#     return wrapper