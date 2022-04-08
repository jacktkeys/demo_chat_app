from flask import Blueprint
from flask_restful import Api

from src.resources import LoginResource

LOGIN_BLUEPRINT = Blueprint("login", __name__)
Api(LOGIN_BLUEPRINT).add_resource(
    LoginResource, "/ping", "/login"
)
