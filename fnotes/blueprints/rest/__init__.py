from flask import Blueprint
from flask_restful import Api

from fnotes.blueprints.rest.resources import NotesResource, SignupResource, LoginResource, NoteResource

api_blueprint = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(api_blueprint)


def init(app):
    api.add_resource(NotesResource, "/notes/")
    api.add_resource(NoteResource, "/notes/<uuid:uuid>")
    api.add_resource(SignupResource, "/signup/")
    api.add_resource(LoginResource, "/login/")

    app.register_blueprint(api_blueprint)
