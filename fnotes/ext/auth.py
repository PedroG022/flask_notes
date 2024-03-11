import bcrypt

from fnotes.model import User
from fnotes.ext.config import config


def verify_login(email, password):
    if not email or not password:
        return False

    user = User.get(email=email)

    if not user:
        return False

    password_hash = bcrypt.hashpw(password.encode('utf-8'), config.get('BCRYPT_HASH'))

    if user.password != password_hash:
        return False

    return True


def user_already_exists(email: str, username: str):
    email_exists = User.get(email=email)
    username_exists = User.get(username=username)

    if email_exists:
        return True

    if username_exists:
        return True

    return False
