from flask import Flask
from flask_restful import Api

# Loading Controllers
from app.controllers.Users import Users
from app.controllers.Posts import Posts

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/api/v1/users')
api.add_resource(Posts, '/api/v1/posts')

if __name__ == '__main__':
    app.run(debug=True)