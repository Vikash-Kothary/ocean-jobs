
from ocean_jobs.visualise.views import views

def register_app(app):
    app.register_blueprint(views)
    pass
