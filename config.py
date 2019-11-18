"""Flask config class."""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """ Flask application config """
    def __init__(self):
            pass

    # Flask settings
    FLASK_ENV = os.environ.get('FLASK_ENV')
    TESTING = os.environ.get('TESTING')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')


    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGO_NAME'),
        'host': os.environ.get('MONGO_ADDR')
    }

    # Flask-User settings
    USER_APP_NAME = "flask-auth-basic"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form

class ProdConfig(Config):
    FLASK_DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_DEBUG = True
    TESTING = True