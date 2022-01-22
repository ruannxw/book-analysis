from flask import Blueprint

apis = Blueprint('apis', __name__)

from .v1 import blueprint as api_v1

apis.register_blueprint(api_v1)
