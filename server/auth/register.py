from flask import request, jsonify, make_response
from flask.views import MethodView
from server import mongo_db, bcrypt, app


class RegisterAPI(MethodView):
    def post(self):
        users = mongo_db.db.users
        login_user = users.find_one({'email': request.json['email']})
        if not login_user:
            try:
                user_name = request.json['name']
                email = request.json['email']
                password = bcrypt.generate_password_hash(
                    request.json['password'], app.config.get('BCRYPT_LOG_ROUNDS')
                ).decode()
                users.insert({'name': user_name, 'email': email, 'password': password})
                response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                }
                return make_response(jsonify(response_object)), 201
            except Exception as e:
                print(e)
                response_object = {
                    'status': 'fail',
                    'message': 'Try again'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(response_object)), 202
