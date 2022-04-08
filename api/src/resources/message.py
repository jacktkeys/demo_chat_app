from flask_restful import Resource
from flask_restful.reqparse import Argument

from src.repositories import MessageRepository
from src.util import parse_params

class MessageResource(Resource):
    @staticmethod
    @parse_params(
        Argument("text", location="json", required=True, help="Text of the new message to create."),
        Argument("userid", location="json", required=True, help="ID of the user that created the message."),
        Argument("roomid", location="json", required=True, help="ID of the room the message is associated with.")
    )
    def post(text, userid, roomid):
        repo = MessageRepository()

        return repo.create_message(text, userid, roomid)
    
    @staticmethod
    @parse_params(
        Argument("messageid", location="json", required=True, help="ID of the message to delete.")
    )
    def delete(messageid):
        repo = MessageRepository()

        return repo.delete_message(messageid)
