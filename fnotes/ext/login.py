from flask_login import LoginManager

from fnotes.model import db


def init(app):
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return db.User.get(id=user_id)
