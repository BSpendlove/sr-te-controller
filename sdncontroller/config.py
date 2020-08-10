import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sdn.db'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrate')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
