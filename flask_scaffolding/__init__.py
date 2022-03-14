# from flask import Flask
# app = Flask(__name__)

# import flask_scaffolding.views

import os

from flask import Flask

# https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS = "false"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from .db import db
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    with app.app_context():
        # a simple page that says hello
        @app.route('/hello')
        def hello():
            return 'Hello, World!'

        from . import routes

        # Import Dash application
        from .dashboard.dashboard import init_dashboard
        app = init_dashboard(app)

        return app

