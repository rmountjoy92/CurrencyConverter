import logging
from flask import Flask
from flask_restx import Api
from app.config import config
from app.currency_converter import CurrencyConverter


# set up rest-x
# https://flask-restx.readthedocs.io/en/latest/quickstart.html
authorizations = {"basic_auth": {"type": "basic"}}
restx = Api(
    version="0.0",
    title="API",
    description="API Description",
    authorizations=authorizations,
    prefix="/api/",
    doc="/api/",
)

# initialize the currency converter
currency_converter = CurrencyConverter()


# Lazily initialize the flask extensions
def register_extensions(app):
    restx.init_app(app)


# register the blueprint modules
def register_blueprints(app):
    from app.api import api

    app.register_blueprint(api, url_prefix="/api")

    from app.site import site

    app.register_blueprint(site)


def create_app(config_name):
    """
    Factory to create Flask application context using config option found in
    app.config

    :param config_name: (string) name of the chosen config option
    :return app: (Flask application context)
    """
    logging.basicConfig(
        filename="app.log",
        filemode="w",
        format="%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    logging.info("App initialized.")
    register_extensions(app)
    register_blueprints(app)

    return app
