# This is the configuration file for the Flask app. Go here for options:
# https://flask.palletsprojects.com/en/1.1.x/config/

# before you start the server, set the CONFIG env variable to select one of these
# options: default, dev, prod, test
# example:
# export CONFIG=dev


class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True


config = {
    "default": DevelopmentConfig,
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig,
}
