import json
from flask import Flask

from controllers.transactions_controller import transaction_bp
from controllers.overview_controller import overview_bp

app = Flask(__name__)

app.register_blueprint(overview_bp)
app.register_blueprint(transaction_bp)

if __name__ == "__main__":
    app.run(debug=True)
