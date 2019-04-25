from flask import Flask
from flask_migrate import Migrate
from .model import configure_db
from .serializer import congigure_serializer as config_se


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/ingresse.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    configure_db(app)
    config_se(app)

    Migrate(app, app.db)

    from .user import blue_print_user

    app.register_blueprint(blue_print_user)

    return app
