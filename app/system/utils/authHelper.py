from app.models.AuthSignInModel import AuthSignInModel
import uuid

class AuthHelper():

  model = None

  def __init__(self):
    """
    Sets AuthModel instance.
    :return:
    """
    self.model = AuthSignInModel()

  def checkToken(self, id):
    """
    Checks is token valid.
    :param id:
    :return:
    """
    try:
      if (self.model.checkToken(id) != None):
        return True
      else:
        return False
    except Exception as e:
      return e.message

  def _generateToken(self):
    """
    Generates token.
    :return: uuid token.
    """
    return uuid.uuid4().hex

  def setToken(self, username):
    if username:
      token = self._generateToken()
      result = self.model.setToken(username, token)
      if result:
        return token
      else:
        return False
