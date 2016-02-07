__version__ = "$Revision$"

from app.system.Database import Database
from app.system.utils.authHelper import AuthHelper
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

class UsersModel(Database):
  # Collection
  collection = None
  authHelper = None

  def __init__(self):
    """

    :return:
    """
    Database.__init__(self)
    self.collection = self.db['users']
    self.authHelper = AuthHelper()

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
    """
    Delete user from DB by unique ID.
    :param id: String. User unique ID.
    :return: String.
    """
    result = self.collection.delete_many({'_id': ObjectId(id)})
    return dumps(result.deleted_count)

  def _checkUser(self, username, password):
    """
    Checks is user registered. If user exists
    return saved to db auth_token.
    :param username: string Username.
    :param password: string Password.
    :return: json
    """
    result = self.collection.find({"username": username})
    for document in result:
      if document['password'] == password and document['username'] == username:
        token = self.authHelper.setToken(document['username'])
        if token:
          return token
        else:
          return False

  def searchUser(self, id):
    """
    Search user in DB by unique ID.
    :param id: String. User unique id.
    :return: String. Username.
    """
    result = self.collection.find_one({"_id": ObjectId(id)})
    return result['username']