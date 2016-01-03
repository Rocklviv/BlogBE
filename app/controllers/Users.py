__version__="$Revision$"

import json, re
from flask import request, jsonify
from flask_restful import Resource
from app.models.UsersModel import UsersModel

#
# TODO: Create a method that would generate CSRF.
#

class Users(Resource):
    model = None

    def __init__(self):
        self.model = UsersModel()

    def get(self):
        result = self.model.list()
        return {"status": 0, "message": "List of Users", "result": json.loads(result)}

    def post(self):
        try:
          username = re.sub(r'^"|"$', '', json.dumps(request.json.get('username')))
          password = re.sub(r'^"|"$', '', json.dumps(request.json.get('password')))
          if self.model._checkUser(username, password):
            pass
        except Exception as e:
          return jsonify({"status": 1, "message": e.message, "result": []})

    def put(self):
      result = self.model.insert()
      return {"status": 0, "message": "Updated user", "result": result}

    def delete(self):
      try:
        id = re.sub(r'^"|"$', '', request.json.get('id'))
        username = self.model.searchUser(id)
        self.model.deleteUser(id)
        return jsonify({"status": 0, "message": "User %s removed successfully" % username, "result": []})
      except Exception as e:
        return jsonify({"status": 1, "message": e.message, "result": []})