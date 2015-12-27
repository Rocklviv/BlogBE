from app.system.Database import Database
from bson.json_util import dumps

class UsersModel(Database):
  # Collection
  collection = None

  def __init__(self):
    """

    :return:
    """
    Database.__init__(self)
    self.collection = self.db['users']

  def list(self):
    """

    :return: Json result.
    """
    result = self.collection.find()
    return dumps(result)

  def insert(self):
    """
    Inserts new user
    :return: Json result.
    """
    data = {"username": "Rocklviv", "email": "dchekirda@gmail.com"}
    result = self.collection.insert_one(data)
    return dumps(result.inserted_id)
