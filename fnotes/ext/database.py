from fnotes.model import db


def init(app):
    db.bind(**app.config['PONY'])
    db.generate_mapping(create_tables=True)
