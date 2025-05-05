import json
from flask import Flask
from flask_cors import CORS
import os

from controllers.transactions_controller import transaction_bp
from controllers.overview_controller import overview_bp

app = Flask(__name__)

ui_url = os.getenv("UI_URL", "http://localhost:3000")

CORS(app, resources={r"/*": {"origins": ui_url}})

app.register_blueprint(overview_bp)
app.register_blueprint(transaction_bp)

if __name__ == "__main__":
    app.run(debug=True)
