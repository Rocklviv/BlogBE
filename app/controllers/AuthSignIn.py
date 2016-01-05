import json
from flask_restful import Resource
from app.models.AuthSignInModel import AuthSignInModel
from flask import request, jsonify, current_app


class AuthSignIn(Resource):

  def post(self):
    pass

  def _checkToken(self):
    pass