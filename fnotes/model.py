import uuid
from datetime import datetime

from flask_login import UserMixin
from pony.orm import Database, Required, Set, PrimaryKey

db = Database()


class Note(db.Entity):
    uuid = PrimaryKey(uuid.UUID, auto=True)
    title = Required(str)
    body = Required(str)
    user = Required('User')
    updated_at = Required(datetime)
    created_at = Required(datetime)


class User(db.Entity, UserMixin):
    uuid = PrimaryKey(uuid.UUID, auto=True)
    username = Required(str, unique=True)
    email = Required(str, unique=True)
    password = Required(bytes)
    role = Required(str)
    notes = Set('Note')
