import os

# storing config items are stored in a class variable for extensibility
class Config(object):
    # placeholder key for dev, prefer environment variable,
    # update to real key later
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'