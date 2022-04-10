from flask import Blueprint
from flask_restful import Api

from src.resources import RoomResource

ROOM_BLUEPRINT = Blueprint("room", __name__)
Api(ROOM_BLUEPRINT).add_resource(
    RoomResource, "/room", "/room/<string:roomid>"
)
