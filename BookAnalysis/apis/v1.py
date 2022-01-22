from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint('api_v1', __name__, url_prefix='/v1')

api = Api(
    blueprint,
    version='1.0',
    title='Book Analysis',
    description='Book Analysis Api'
)

from .namespaces.data import ns as ns_data

api.add_namespace(ns_data)
