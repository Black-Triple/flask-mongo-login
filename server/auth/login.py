from flask import request, jsonify, make_response
from flask.views import MethodView
from server import mongo_db, bcrypt, models


class LoginAPI(MethodView):
    def post(self):
        try:
            users = mongo_db.db.users
            login_user = users.find_one({'email': request.json['email']})

            if login_user:
                if bcrypt.check_password_hash(login_user['password'], request.json['password']):
                    auth_token = models.encode_auth_token(str(login_user['_id']))
                    if auth_token:
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'auth_token': auth_token.decode()
                        }
                        return make_response(jsonify(response_object)), 200
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'Please enter valid email or password.'
                    }
                return make_response(jsonify(response_object)), 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(response_object)), 404

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(response_object)), 500
