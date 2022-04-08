from flask import Blueprint
from flask_restful import Api

from src.resources import RoomResource, RoomsResource

ROOM_BLUEPRINT = Blueprint("room", __name__)
Api(ROOM_BLUEPRINT).add_resource(
    RoomResource, "/room", "/room/<string:roomid>"
)

ROOMS_BLUEPRINT = Blueprint("rooms", __name__)
Api(ROOMS_BLUEPRINT).add_resource(
    RoomsResource, "/rooms"
)
