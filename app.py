import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# Loading Controllers
from app.system.utils import get_instance_folder_path, get_app_base_path
from config.config import configure_app
from app.controllers.Users import Users
from app.controllers.Posts import Posts
from app.controllers.AuthSignIn import AuthSignIn

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True)
api = Api(app)
configure_app(app)
CORS(app, resources={r'/api/*':{'origins': '*'}})

api.add_resource(Users, '/api/v1/users')
api.add_resource(Posts, '/api/v1/posts')

if __name__ == '__main__':
    app.run()