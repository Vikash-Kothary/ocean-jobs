from flask import Blueprint

status = Blueprint("status", __name__)


@status.route("/ping")
def ping():
    return "The service is up."
