from ocean_jobs.visualisations.views import views


def register_app(app):
    app.register_blueprint(views, url_prefix="/")
    pass
