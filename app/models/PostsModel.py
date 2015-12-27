from app.system.Database import Database
from bson.json_util import dumps

class PostsModel(Database):

  collection = None

  def __init__(self):
    Database.__init__(self)
    self.collection = self.db['posts']

  def getPosts(self):
    result = self.collection.find()
    return dumps(result)

  def insertPost(self, data):
    try:
      result = self.collection.insert_one(data)
      return dumps(result.inserted_id)
    except Exception as e:
      return e.message