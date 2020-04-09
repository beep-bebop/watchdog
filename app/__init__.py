from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.resource.video import Video
from app.resource.sensors import Sensors
from app.resource.login import Login
from app.resource.register import Register

app = Flask(__name__)
CORS(app, supports_credentials=True)

#api列表
api = Api(app)
api.add_resource(Video, '/api/video')
api.add_resource(Sensors, '/api/sensors')
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')