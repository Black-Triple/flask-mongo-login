from flask import request, jsonify, make_response
from flask.views import MethodView
from server import mongo_db, models
import jwt
from bson.objectid import ObjectId


class UserAPI(MethodView):
    def get(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                response_object = {
                    'status': 'fail',
                    'message': 'JWT token malformed'
                }
                return make_response(jsonify(response_object)), 401
        else:
            auth_token = ''

        if auth_token:
            try:
                resp = models.decode_auth_token(auth_token)
                user = mongo_db.db.users.find_one({'_id': ObjectId(resp)})
                response_object = {
                    'status': 'success',
                    'data': {
                        'name': user['name'],
                        'email': user['email']
                    }
                }
                return make_response(jsonify(response_object)), 200
            except jwt.ExpiredSignatureError:
                message = 'Signature expired. Please log in again.'
            except jwt.InvalidTokenError:
                message = 'Invalid token. Please log in again.'
            response_object ={
                'status': 'fail',
                'message': message
            }
            return make_response(jsonify(response_object)), 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(response_object)), 401




