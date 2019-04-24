from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha512

db = SQLAlchemy()


def configure_db(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    date_of_birth = db.Column(db.DateTime())

    def password_hash(self):
        self.password = pbkdf2_sha512.hash(self.password)

    def password_veification(self, password):
        return pbkdf2_sha512.verify(password, self.password)
