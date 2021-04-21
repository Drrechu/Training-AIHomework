
from flask_restplus import Resource, Namespace

ns = Namespace('health')


@ns.route('/')
class Health(Resource):

    def get(self):
        return {}, 200