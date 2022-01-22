import os

from . import prefix, basedir
from .BaseConfig import BaseConfig


class ProductionConfig(BaseConfig):
    ENV = 'production'