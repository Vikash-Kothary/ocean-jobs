from ocean_jobs.data.data import data


def register_app(app):
    app.register_blueprint(data, url_prefix="/data", cli_group=None)
