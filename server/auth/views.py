from flask import Blueprint
from server.auth.login import LoginAPI
from server.auth.register import RegisterAPI
from server.auth.showInfo import UserAPI
from server.auth.logout import LogoutAPI

auth_blueprint = Blueprint('auth', __name__)

login_view = LoginAPI.as_view('login_api')
register_view = RegisterAPI.as_view('register_api')
user_view = UserAPI.as_view('user_api')
logout_view = LogoutAPI.as_view('logout_api')

auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=register_view,
    methods=['POST']
)

auth_blueprint.add_url_rule(
    '/auth/showUser',
    view_func=user_view,
    methods=['GET']
)

auth_blueprint.add_url_rule(
    '/auth/logout',
    view_func=logout_view,
    methods=['POST']
)
