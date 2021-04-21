from flask_restplus import Resource, Namespace
import requests
from flask import request

ns = Namespace('api/v1')


@ns.route('/ping')
class Ping(Resource):

    def post(self):
        url = request.json["url"]
        response = requests.get(url=url, verify=False)

        response.raise_for_status()

        return response.json()
