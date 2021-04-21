from flask import Flask
from service1.api.api_base import blueprint as api_blueprint
from flasgger import Swagger
import pathlib


def run_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.register_blueprint(api_blueprint)
    setup_openapi(app)
    app.run(host="0.0.0.0", port=8080, debug=True)


def setup_openapi(app):
    openapi_path = str(pathlib.Path(__file__).parent.absolute()) + '/api/openapi.yml'
    Swagger(app, template_file=openapi_path, parse=True)


run_app()
