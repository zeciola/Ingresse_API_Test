from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from .model import User
from .serializer import UserSchema
from datetime import timedelta

blue_print_login = Blueprint("login", __name__)


@blue_print_login.route("/login", methods=["POST"])
def login():

    user, error = UserSchema().load(request.json)

    if error:
        return jsonify(error), 401
    elif "date_of_birth" in request.json.keys():
        return jsonify({"Error": "Please dont send date_of_birth to login"}), 401

    user = User.query.filter_by(username=user.username).first()

    if user and user.password_verification(request.json["password"]):
        acess_token = create_access_token(
            identity=user.id, expires_delta=timedelta(seconds=1)
        )

        refresh_token = create_refresh_token(identity=user.id)

        return (
            jsonify(
                {
                    "acess_token": acess_token,
                    "refresh_token": refresh_token,
                    "msg": "sucess",
                }
            ),
            200,
        )

    return (
        jsonify({"msg": "Invalid credentials, please insert a valid credential"}),
        401,
    )
