from app.system.Database import Database
from bson.json_util import dumps
from bson.objectid import ObjectId

class PostsModel(Database):

  collection = None

  def __init__(self):
    """

    :return:
    """
    Database.__init__(self)
    self.collection = self.db['posts']

  def getPosts(self):
    """

    :return:
    """
    result = self.collection.find()
    return dumps(result)

  def getPost(self, id):
    """

    :param id:
    :return:
    """
    result = self.collection.find_one({"_id": ObjectId(id)})
    return dumps(result)

  def insertPost(self, data):
    """

    :param data:
    :return:
    """
    try:
      result = self.collection.insert_one(data)
      return dumps(result.inserted_id)
    except Exception as e:
      return e.message