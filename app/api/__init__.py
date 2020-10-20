from flask import Blueprint

api = Blueprint("api", __name__)


# this gets overwritten by rest-x
@api.route("/", methods=["GET"])
def root():
    return ""


from . import endpoints
