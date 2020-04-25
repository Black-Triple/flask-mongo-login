import datetime
import jwt
from server import app
from server.auth import blacklist_token


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :param user_id:
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
    is_blacklisted_token = blacklist_token.check_blacklist_token(auth_token)
    if is_blacklisted_token:
        raise jwt.InvalidTokenError('Please re-login to access the page')
    else:
        return payload['sub']
