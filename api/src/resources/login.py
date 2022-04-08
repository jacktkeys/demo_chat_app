from flask_restful import Resource
from flask_restful.reqparse import Argument

from src.repositories.user import UserRepository
from src.util.parse_params import parse_params

class LoginResource(Resource):
    @staticmethod
    def get():
        return "pong"

    @staticmethod
    @parse_params(
        Argument("username", location="json", required=True, help="Username to authenticate.")
    )
    def post(username):
        repo = UserRepository()

        return repo.authenticate(username)
