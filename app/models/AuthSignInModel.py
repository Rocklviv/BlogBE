from app.system.Database import Database
from bson.json_util import dumps
from bson.objectid import ObjectId

class AuthSignInModel(Database):

  collection = None

  def __init__(self):
    Database.__init__(self)
    self.collection = self.db['auth']

  def checkToken(self, token):
    result = self.collection.find_one({"token": ObjectId(token)})

    pass

  def _checkTime(self, time):
    pass