from flask import Flask
from controllers.transaction_controller import transaction_bp

app = Flask(__name__)

app.register_blueprint(transaction_bp)

if __name__ == "__main__":
    app.run(debug=True)
