
from flask import Flask

from ocean_jobs import status
from ocean_jobs import data
from ocean_jobs import features
from ocean_jobs import modelling
from ocean_jobs import visualise

def create_app():
    app = Flask(__name__)
    status.register_app(app)
    data.register_app(app)
    features.register_app(app)
    modelling.register_app(app)
    visualise.register_app(app)
    return app

if __name__ == '__main__':
    create_app()
