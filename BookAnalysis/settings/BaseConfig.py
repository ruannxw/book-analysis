import os

from . import basedir


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'e6fd6e41-ef5b-4796-8b22-641f7b2d7392')
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True

    RESTX_MASK_SWAGGER = False
