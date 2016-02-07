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
      if (request.is_xhr):
        username = request.json.get('username')
        password = request.json.get('password')
        result = self.model._checkUser(username, password)
        if result:
          print result
          response = jsonify({"status": 0, "message": "Logged in as: %s" % username, "result": [ {"token": result} ]})
          response.status_code = 200
          return  response
        else:
          response = jsonify({"status": 1, "message": "Username or password is incorect.", "result": []})
          response.status_code = 403
          return response
      else:
        print "Not XHR"

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