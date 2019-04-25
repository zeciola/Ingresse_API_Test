from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .model import configure_db
from .serializer import congigure_serializer as config_se


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/ingresse.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config[
        "JWT_SECRET_KEY"
    ] = "Ingresse o melhor lugar para comprar seus ingressos!"

    configure_db(app)
    config_se(app)

    Migrate(app, app.db)

    JWTManager(app)

    from .user import blue_print_user

    app.register_blueprint(blue_print_user)

    from .user_login import blue_print_user_login

    app.register_blueprint(blue_print_user_login)

    return app
