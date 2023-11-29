from os import environ, path
from datetime import timedelta


class Config(object):
    """ Base configurations class """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
