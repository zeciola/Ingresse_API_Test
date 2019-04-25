from flask import Blueprint, jsonify, request, current_app
from .serializer import UserSchema
from .model import User

blue_print_user = Blueprint("user", __name__)

# Mostrar todos


@blue_print_user.route("/show", methods=["GET"])
def show():

    result = User.query.all()

    return UserSchema(many=True).jsonify(result), 200


# Mostrar por id


@blue_print_user.route("/show_by_id/<identificator>", methods=["GET"])
def show_by_id(identificator):

    result = User.query.filter(User.id == identificator)

    return UserSchema(many=True).jsonify(result), 200


# Registar


@blue_print_user.route("/register_user", methods=["POST"])
def create():
    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.password_hash()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201


# Mudar por id


@blue_print_user.route("/change_by_id/<identificator>", methods=["POST"])
def change(identificator):
    us = UserSchema()
    query = User.query.filter(User.id == identificator)

    if us.jsonify(query.first()).get_json() == {}:
        return jsonify("Error not found user id"), 401

    query.update(request.json)
    current_app.db.session.commit()

    return us.jsonify(query.first())


# Mudar por id


@blue_print_user.route("/change_by_username/<identificator>", methods=["GET", "PUT"])
def change_username(identificator):

    us = UserSchema()
    query = User.query.filter(User.username == identificator)
    if us.jsonify(query.first()).get_json() == {}:
        return jsonify("Error not found user"), 401
    query.update(request.json)
    current_app.db.session.commit()

    return jsonify(f"The user {identificator} has been modified"), 200


# Deletar por id


@blue_print_user.route("/delete_by_id/<identificator>", methods=["GET", "DELETE"])
def delete_id(identificator):

    us = UserSchema()
    query = User.query.filter(User.username == identificator)

    # import ipdb; ipdb.set_trace()

    if us.jsonify(query.first()).get_json() == {}:
        return jsonify("Error not found user id"), 401

    User.query.filter(User.id == identificator).delete()
    current_app.db.session.commit()

    return jsonify(f"The user for id: {identificator} has been deleted"), 200
