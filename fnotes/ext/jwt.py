from flask_jwt_extended import JWTManager
from fnotes.model import User


def init(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        if isinstance(user, User):
            return user.email
        else:
            # Email
            return user

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.select(lambda u: u.email == identity).get()
