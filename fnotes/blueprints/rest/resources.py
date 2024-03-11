from datetime import datetime

import bcrypt
from flask import jsonify, request
from flask_jwt_extended import *
from flask_restful import Resource
from pony.orm import select, db_session
from pony.orm.core import Query

from fnotes.ext.auth import user_already_exists, verify_login
from fnotes.ext.config import config
from fnotes.model import Note, User


class SignupResource(Resource):
    @staticmethod
    def post():
        body = request.get_json()

        email: str = body['email']
        username: str = body['username']
        password: str = body['password']

        if user_already_exists(email, username):
            return 'This user already exists.', 409

        password_hash = bcrypt.hashpw(password.encode('utf-8'), config.get('BCRYPT_HASH'))

        with db_session:
            user = User(email=email, username=username, password=password_hash, role='user')
            return str(user.uuid), 201


class LoginResource(Resource):
    @staticmethod
    def post():
        body = request.get_json()

        email: str = body['email']
        password: str = body['password']

        if not verify_login(email, password):
            return 'Invalid credentials', 401

        access_token = create_access_token(identity=email)

        return access_token, 200


class NotesResource(Resource):

    @jwt_required()
    def get(self):
        notes: Query = select(n for n in Note if n.user.uuid == current_user.uuid)

        return jsonify(
            [note.to_dict() for note in notes]
        )

    @jwt_required()
    def post(self):
        body = request.get_json()

        title = body['title']
        body = body['body']

        created_at = datetime.now()
        updated_at = datetime.now()

        user = current_user

        note = Note(title=title, body=body, created_at=created_at, updated_at=updated_at, user=user)
        note.flush()

        return str(note.uuid), 201


class NoteResource(Resource):
    @jwt_required()
    def get(self, uuid):
        note: Note = Note.get(lambda n: n.uuid == uuid and current_user.uuid == n.user.uuid)

        if not note:
            return 'Note not found', 404

        return jsonify(note.to_dict())

    @jwt_required()
    def delete(self, uuid):
        note: Note = Note.get(lambda n: n.uuid == uuid and current_user.uuid == n.user.uuid)

        if not note:
            return 'Note not found', 404

        note.delete()

    @jwt_required()
    def patch(self, uuid):
        note: Note = Note.get(lambda n: n.uuid == uuid and current_user.uuid == n.user.uuid)

        if not note:
            return 'Note not found', 404

        request_body = request.get_json()

        title = request_body['title']
        body = request_body['body']
        updated_at = datetime.now()

        note.set(title=title, body=body, updated_at=updated_at)

        return '', 200
