from flask import current_app
from config.config import DevConfig
from pymongo import MongoClient

class Database(DevConfig):
  """
  Main Database class
  """
  # Database name
  db = None
  # MongoDB Client
  client = None
  # MongoDB URL
  url = DevConfig.MONGODBURL

  def __init__(self):
    """
    Init mongo connect.
    :return:
    """
    self.client = MongoClient('mongodb://%s' % self.url)
    self.db = self.client['test']