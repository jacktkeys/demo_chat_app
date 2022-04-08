from flask import Blueprint
from flask_restful import Api

from src.resources import UserResource

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user"
)
