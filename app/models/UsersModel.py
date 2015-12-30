import json
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
    data = {"username": "Rocklviv", "email": "dchekirda@gmail.com", "password": "762307"}
    result = self.collection.insert_one(data)
    return dumps(result.inserted_id)

  def deleteUser(self, id):
    result = self.collection.delete_many({'_id': str(id)})
    print dumps(result.deleted_count)

  def _checkUser(self, username, password):
    """
    Checks is user registered. If user exists
    return saved to db auth_token.
    :param username: string Username.
    :param password: string Password.
    :return: json
    """
    result = self.collection.find({"username": username, "password": password})
    print(dumps(result))