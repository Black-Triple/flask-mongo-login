from flask import request, jsonify, make_response
from flask.views import MethodView
from server import mongo_db, models
import datetime


class LogoutAPI(MethodView):
    def post(self):
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
                if resp is not None:
                    blacklist_tokens = mongo_db.db.blacklist_tokens
                    blacklist_tokens.insert({'token': auth_token, 'createdAt': datetime.datetime.now()})
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return make_response(jsonify(response_object)), 200
            except Exception as e:
                response_object = {
                    'status': 'fail',
                    'message': e
                }
                return make_response(jsonify(response_object)), 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(response_object)), 403
