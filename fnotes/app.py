from flask import Flask
from flask_cors import CORS
from pony.flask import Pony

from fnotes.blueprints import rest, web
from fnotes.ext import database, jwt
from fnotes.ext.config import config


def create_app():
    app = Flask(__name__)
    app.config.update(config)

    Pony(app)
    CORS(app)

    database.init(app)
    jwt.init(app)
    rest.init(app)
    web.init(app)

    return app
