from flask import Flask
from flask_cors import CORS

from database.config import connect_to_database
import os

from controllers.base_controller import api_bp


def set_cors_policies(app: Flask):
    ui_url = os.getenv("UI_URL", "http://localhost:3000")
    CORS(app, resources={r"/*": {"origins": ui_url}})


def create_app():
    app = Flask(__name__)

    connect_to_database(app)
    set_cors_policies(app)

    app.register_blueprint(api_bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
