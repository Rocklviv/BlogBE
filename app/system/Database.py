from pymongo import MongoClient

class Database():
  """
  Main Database class
  """
  # Database name
  db = None
  # MongoDB Client
  client = None
  # MongoDB URL
  url = '192.168.99.100'

  def __init__(self):
    """
    Init mongo connect.
    :return:
    """
    self.client = MongoClient('mongodb://%s' % self.url)
    self.db = self.client['test']