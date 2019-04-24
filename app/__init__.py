from flask import Flask
from flask_migrate import Migrate
from .model import configure_db


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/ingresse.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_db(app)

    Migrate(app, app.db)

    return app
