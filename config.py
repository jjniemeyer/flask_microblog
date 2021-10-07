import os
basedir = os.path.abspath(os.path.dirname(__file__))
# config items are stored in a class variable for extensibility
class Config(object):
    # placeholder key for dev, prefer environment variable,
    # update to real key later
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
