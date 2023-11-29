from flask import Flask
from flask_cors import CORS

from routes.api import api


def create_app(config="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(api)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.errorhandler(Exception)
    def error_handler(error):
        code = getattr(error, "code", 500)
        description = getattr(error, "description", "Server Error")
        return {"message": description}, code if code is int else 500

    return app
