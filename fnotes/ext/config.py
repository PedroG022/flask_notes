import os.path

config = dict(
    DEBUG=False,
    JWT_SECRET_KEY='secret_xyz',
    SECRET_KEY='secret_xyz',
    PONY={
        'provider': 'sqlite',
        'filename': os.path.join(os.getcwd(), 'db.sqlite'),
        'create_db': True
    },
    BCRYPT_HASH=bytes(os.getenv('BCRYPT_HASH'), 'utf-8'),
)
