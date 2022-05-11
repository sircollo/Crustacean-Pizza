import os

class Config:
  pass


class TestConfig(Config):
  pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
}