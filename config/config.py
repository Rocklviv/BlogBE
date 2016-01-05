import os
import logging

class BaseConfig(object):
  DEBUG = False
  LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  #LOGGING_LOCATION = 'app.log'
  LOGGING_LEVEL = logging.DEBUG
  MONGODBURL = ''
  MONGODBUSER = ''
  MONGODBPASS = ''


class DevConfig(BaseConfig):
  DEBUG = True
  MONGODBURL = '192.168.99.100' # on windows machine due to docker usage url will be 192.168.99.100


class StageConfig(BaseConfig):
  DEBUG = False
  MONGODBURL = ''
  MONGODBUSER = ''
  MONGODBPASS = ''

config = {
  "development": "config.config.DevConfig",
  "stage": "config.config.StageConfig",
  "default": "config.config.DevConfig"
}

def configure_app(app):
  config_name = os.getenv('FLASK_CONFIGURATION', 'default')
  app.config.from_object(config[config_name])
  app.config.from_pyfile('config.cfg', silent=True)
  # Configure logging
  #handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
  #handler.setLevel(app.config['LOGGING_LEVEL'])
  formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
  #handler.setFormatter(formatter)
  #app.logger.addHandler(handler)