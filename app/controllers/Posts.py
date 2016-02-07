from flask_restful import Resource
from app.models.PostsModel import PostsModel
from flask import request, jsonify, current_app
from app.system.utils.authHelper import AuthHelper
import json

class Posts(Resource):
  # PostsModel instance.
  model = None
  auth = None

  def __init__(self):
    self.model = PostsModel()
    self.auth = AuthHelper()

  def get(self):
    """
    Returns list of posts of post by id.
    :param id: String. Unique ID of post.
    :return:
    """
    id = None
    if not request.args:
      id = None

    if not id:
      result = self.model.getPosts()
      current_app.logger.info('List of posts.')
      return jsonify({"status": 0, "message": "List of posts", "result": result })
    else:
      result = self.model.getPost(id)
      current_app.logger.info('Getting post %s' % id)
      return jsonify({"status": 0, "message": "Post", "result": result})

  def post(self):
    """
    Creates Post inserting required data into MongoDB.
    :return: json
    """
    """
    TODO: Add check if token exists.
    """
    if not request.json:
      return jsonify({"status": 1, "message": "Request should contain a data", "result": []})
    elif not request.json.get('token'):
      response = jsonify({"status": 2, "message": "Authentification required.", "result": []})
      response.status_code = 401
      return response
    else:
      try:
        token = json.dumps(request.json.get('token').replace('"', ""))
        if (self.auth.checkToken(token)):
          title = json.dumps(request.json.get('title')).replace('"', "")
          shortUrl = json.dumps(request.json.get('shortUrl')).replace('"', "")
          shortText = json.dumps(request.json.get('shortText')).replace('"', "")
          longText = json.dumps(request.json.get('longText')).replace('"', "")
          tags = json.dumps(request.json.get('tags')).replace('"', "")
          date = json.dumps(request.json.get('date')).replace('"', "")

          if not type(title) == str:
            msg = ("Field title should be a string")
            return jsonify({"status": 2, "message": msg, "result": []})
          elif not type(shortUrl) == str:
            msg = ("Field shortUrl should be a string")
            return jsonify({"status": 2, "message": msg, "result": []})
          elif not type(shortText) == str:
            msg = ("Field shortText should be a string")
            return jsonify({"status": 2, "message": msg, "result": []})
          elif not type(longText) == str:
            msg = ("Field longText should be a string")
            return jsonify({"status": 2, "message": msg, "result": []})
          elif not type(tags) == str:
            msg = ("Field tags should be a string")
            return jsonify({"status": 2, "message": msg, "result": []})

          data = {"title": title, "shortUrl": shortUrl, "shortText":shortText, "longText":longText, "tags":tags, "date":date}
          result = self.model.insertPost(data)
          return jsonify(result)
      except Exception as e:
        return jsonify({"status": 3, "message": "Authentication failed. Auth token is expired.", "result": [
          {"redirect": "/auth/signin"}
        ]})

  def put(self):
    pass

  def delete(self):
    pass