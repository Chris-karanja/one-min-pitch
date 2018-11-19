import os


class Config:
    SECRET_KEY = os.environ.get('321')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kobura:fbi321@localhost/pitches'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}