from flask import Flask

from ocean_jobs import data, features, models, utils, visualisations


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
