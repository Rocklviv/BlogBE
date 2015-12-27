from flask_restful import Resource
from app.models.PostsModel import PostsModel
from flask import request, jsonify
import json

class Posts(Resource):
  # PostsModel instance.
  model = None

  def __init__(self):
    self.model = PostsModel()

  def get(self):
    result = self.model.getPosts()
    return json.loads(result)

  def post(self):
    if not request.json:
      return jsonify({"status": 1, "message": "Request should contain a data", "result": []})
    else:
      title = json.dumps(request.json.get('title'))
      shortUrl = json.dumps(request.json.get('shortUrl'))
      shortText = json.dumps(request.json.get('shortText'))
      longText = json.dumps(request.json.get('longText'))
      tags = json.dumps(request.json.get('tags'))
      date = json.dumps(request.json.get('date'))

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

  def put(self):
    pass

  def delete(self):
    pass

  def _checkEmail(self, email):
    pass