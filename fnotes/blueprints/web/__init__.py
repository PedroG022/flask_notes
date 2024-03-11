from flask import Blueprint

from fnotes.blueprints.web.views import login, notes

blueprint = Blueprint("Web", __name__, url_prefix="/", template_folder="templates")


def init(app):
    blueprint.add_url_rule('/login', view_func=login)
    blueprint.add_url_rule('/notes', view_func=notes)
    app.register_blueprint(blueprint)
