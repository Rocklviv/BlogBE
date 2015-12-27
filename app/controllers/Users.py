from flask_restful import Resource
from app.models.UsersModel import UsersModel
import json

class Users(Resource):
    model = None

    def __init__(self):
        self.model = UsersModel()

    def get(self):
        result = self.model.list()
        return {"status": 0, "message": "List of Users", "result": json.loads(result)}

    def post(self):
        result = self.model.insert()
        return {"status": 0, "message": "Posted List", "result": json.loads(result)}

    def put(self):
        return {"status": 0, "message": "Updated user"}

    def delete(self):
        return {"status": 0, "message": "User removed successfully"}