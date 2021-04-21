from flask_restplus import Resource, Namespace

ns = Namespace('api/v1/info')


@ns.route("/")
class Info(Resource):

    def get(self):
        return {"Receiver": "Cisco is the best!"}
