from flask_restful import Resource
from flask_restful.reqparse import Argument

from src.repositories import RoomRepository
from src.util import parse_params

class RoomResource(Resource):
    @staticmethod
    def get(roomid=None):
        repo = RoomRepository()
        if roomid is None:
            data = repo.get_rooms()
            val = sorted(data, key=lambda x: '' if x['mostRecentMessage'] is None else x['mostRecentMessage']['sentAt'], reverse=True)
            return val
        else:
            return repo.get_room(roomid)
            

    @staticmethod
    @parse_params(
        Argument("roomname", location="json", required=True, help="Name to giv the new room."),
        Argument("userid", location="json", required=True, help="ID of the user creating the room.")
    )
    def post(roomname, userid):
        repo = RoomRepository()

        return repo.create_room(roomname, userid)

    @staticmethod
    @parse_params(
        Argument("roomid", location="json", required=True, help="ID of the room to delete.")
    )
    def delete(roomid):
        repo = RoomRepository()

        return repo.delete_room(roomid)
