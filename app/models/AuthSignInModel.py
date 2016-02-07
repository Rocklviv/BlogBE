from app.system.Database import Database
from bson.json_util import dumps
from bson.objectid import ObjectId

class AuthSignInModel(Database):

  collection = None

  def __init__(self):
    Database.__init__(self)
    self.collection = self.db['auth']

  def checkToken(self, token):
    result = self.collection.find_one({"token": token})
    if result:
      return True
    else:
      return False

  def _checkTime(self, time):
    pass

  def setToken(self, username, token):
    result = self.collection.insert_one({"username": username, "token": token})
    return result.inserted_id