import os

os.environ['BCRYPT_HASH'] = '$2b$12$WkJ6xukTP179uMNh5CLGQ.'

from fnotes.app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
