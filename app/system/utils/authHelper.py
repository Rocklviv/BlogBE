from app.models.AuthSignInModel import AuthModel

class AuthHelper():

  model = None

  def __init__(self):
    """
    Sets AuthModel instance.
    :return:
    """
    self.model = AuthModel()

  def checkToken(self, id):
    """
    Checks is token valid.
    :param id:
    :return:
    """
    try:
      self.model.checkToken(id)
    except Exception as e:
      return e.message