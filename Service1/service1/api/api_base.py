from flask import Blueprint
from flask_restplus import Api

from service1.api.health import ns as health_ns
from service1.api.ping import ns as ping_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='Service1')

api.add_namespace(ping_ns)
api.add_namespace(health_ns)
