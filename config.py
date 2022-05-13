import os

class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SECRET_KEY = 'hiiniformstu'
  UPLOADED_PHOTOS_DEST ='app/static/photos'



class TestConfig(Config):
  pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/pizzadb'
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adeh:adeh123!@localhost/pizzadb'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/pizzadb'
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://teresiah:1234@localhost/pizzadb'
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
}