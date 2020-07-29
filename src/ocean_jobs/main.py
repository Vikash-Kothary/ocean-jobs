from flask import Flask

from ocean_jobs import data
from ocean_jobs import features
from ocean_jobs import models
from ocean_jobs import visualisations
from ocean_jobs import utils


def create_app():
    app = Flask(__name__)
    data.register_app(app)
    features.register_app(app)
    models.register_app(app)
    visualisations.register_app(app)
    utils.register_app(app)
    return app


if __name__ == "__main__":
    create_app()
