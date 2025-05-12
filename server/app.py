from flask import Flask
from flask_cors import CORS
import os

from controllers.base_controller import api_bp

app = Flask(__name__)

ui_url = os.getenv("UI_URL", "http://localhost:3000")

CORS(app, resources={r"/*": {"origins": ui_url}})

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
