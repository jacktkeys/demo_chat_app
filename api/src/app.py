from flask import Flask, Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS

from src.routes import USER_BLUEPRINT
from src.routes import ROOM_BLUEPRINT
from src.routes import ROOMS_BLUEPRINT
from src.routes import MESSAGE_BLUEPRINT
from src.routes import LOGIN_BLUEPRINT

app = Flask(__name__)
CORS(app)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

app.register_blueprint(USER_BLUEPRINT)
app.register_blueprint(ROOM_BLUEPRINT)
app.register_blueprint(ROOMS_BLUEPRINT)
app.register_blueprint(MESSAGE_BLUEPRINT)
app.register_blueprint(LOGIN_BLUEPRINT)

app.register_blueprint(api_bp)
