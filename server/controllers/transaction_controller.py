from flask import Blueprint, jsonify

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transactions")


@transaction_bp.route("/", methods=["GET"])
def get_transactions():
    return jsonify({"name": "transactions"})
