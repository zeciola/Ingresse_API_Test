from flask import Blueprint, jsonify, request, current_app
from .serializer import UserSchema
from .model import User
from flask_jwt_extended import jwt_required


blue_print_user = Blueprint("user", __name__)


@blue_print_user.route("/")
def defalt():
    return jsonify({"Ingresse API Online": True})


# Mostrar todos


@blue_print_user.route("/show", methods=["GET"])
@jwt_required
def show():

    result = User.query.all()

    return UserSchema(many=True).jsonify(result), 200


# Mostrar por id


@blue_print_user.route("/show_by_id/<identificator>", methods=["GET"])
@jwt_required
def show_by_id(identificator):

    result = User.query.filter(User.id == identificator)

    return UserSchema(many=True).jsonify(result), 200


# Registar


@blue_print_user.route("/register_user", methods=["POST"])
def register():
    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.password_hash()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201


# Mudar por id


@blue_print_user.route("/change_by_id/<identificator>", methods=["PUT"])
@jwt_required
def change_id(identificator):
    us = UserSchema()
    query = User.query.filter(User.id == identificator)

    if us.jsonify(query.first()).get_json() == {}:
        return jsonify(f"Error not found user {identificator}"), 401

    query.update(request.json)
    current_app.db.session.commit()

    return us.jsonify(query.first())


# Deletar por id


@blue_print_user.route("/delete_by_id/<identificator>", methods=["DELETE"])
@jwt_required
def delete_id(identificator):

    us = UserSchema()
    query = User.query.filter(User.id == identificator)

    # import ipdb; ipdb.set_trace()

    if us.jsonify(query.first()).get_json() == {}:
        return jsonify(f"Error not found user id: {identificator}"), 401

    User.query.filter(User.id == identificator).delete()
    current_app.db.session.commit()

    return jsonify(f"The user for id: {identificator} has been deleted"), 200
