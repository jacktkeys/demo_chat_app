"""
Defines the blueprint for the messages
"""
from flask import Blueprint
from flask_restful import Api

from src.resources import MessageResource

MESSAGE_BLUEPRINT = Blueprint("message", __name__)
Api(MESSAGE_BLUEPRINT).add_resource(
    MessageResource, "/message"
)