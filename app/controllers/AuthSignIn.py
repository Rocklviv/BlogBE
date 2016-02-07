import json
from flask_restful import Resource
from app.models.AuthSignInModel import AuthSignInModel
from flask import request, jsonify, current_app


class AuthSignIn(Resource):

  model = None

  def __init__(self):
    self.model = AuthSignInModel()

  def post(self):
    try:
      if (request.is_xhr):
        username = json.dumps(request.json.get('username'))
        password = json.dumps(request.json.get('password'))

        result = self.model.checkUser(username, password)
        if (result):
          response = jsonify({"status": 0, "message": "Logged in as: %s", "result": [
            {"token": result.token}
          ]}) % result.userGroup
          response.status_code = 200
          return  response
        else:
          response = jsonify({"status": 1, "message": "Username or password is incorect.", "result": []})
          response.status_code = 403
          return response
    except Exception as e:
      respons = jsonify({"status": 4, "message": "Bad request", "result": []})
      respons.status_code = 400
      return respons

  def _setToken(self):
    pass