import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to  guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGOENGINE_DATABASE_URI = ''


class TestingConfig(Config):
    TESTING = True
    MONGOENGINE_DATABASE_URI = ''


class ProductionConfig(Config):
    MONGOENGINE_DATABASE_URI = ''

Config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
