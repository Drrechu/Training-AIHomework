from flask import Blueprint
from flask_restplus import Api

from receiver_service.api.info import ns as info_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='Receiver')

api.add_namespace(info_ns)
