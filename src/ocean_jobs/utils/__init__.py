
from ocean_jobs.utils.status import status

def register_app(app):
    app.register_blueprint(status, url_prefix='/')