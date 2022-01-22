import os

from . import prefix, basedir
from .BaseConfig import BaseConfig


class TestConfig(BaseConfig):
    ENV = 'testing'
    TESTING = True