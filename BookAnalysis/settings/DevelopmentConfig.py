import os

from . import basedir, prefix
from .BaseConfig import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    # SQLALCHEMY_ECHO = True
