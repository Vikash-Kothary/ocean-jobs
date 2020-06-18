from flask import Blueprint

status = Blueprint('status', __name__)

def register_app(app):
    app.register_blueprint(status)

@status.route('/ping')
def ping():
    return 'The service is up.'

