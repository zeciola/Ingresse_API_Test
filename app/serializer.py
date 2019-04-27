from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import User

ma = Marshmallow()


def congigure_serializer(app):
    ma.init_app(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    date_of_birth = fields.Date(required=False)

    @validates("id")
    def validate_id(self, value):
        raise ValidationError("Please, dont send id")
