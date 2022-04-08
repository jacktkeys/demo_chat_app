from flask_restful import Resource
from flask_restful.reqparse import Argument

from src.repositories import UserRepository
from src.util.parse_params import parse_params

class UserResource(Resource):
    @staticmethod
    @parse_params(
        Argument("username", location="json", required=True, help="Username to create.")
    )
    def post(username):
        repo = UserRepository()

        return repo.create_user(username)
