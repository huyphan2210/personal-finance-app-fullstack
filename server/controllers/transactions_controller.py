from http import HTTPStatus
from flask import jsonify
from flask_restx import Namespace, Resource, reqparse

from services.transactions_service import get_transactions
from models.transactions_model import TransactionsContent

TRANSACTIONS = "transactions-api"
transactions_ns = Namespace(f"{TRANSACTIONS}", description="Get Transactions content")

get_transaction_query_parser = reqparse.RequestParser()
get_transaction_query_parser.add_argument("page", type=int, default=1)
get_transaction_query_parser.add_argument("search", type=str, default="")
get_transaction_query_parser.add_argument("category", type=str, default="")
get_transaction_query_parser.add_argument("sortBy", type=str, default="")


class TransactionsApi(Resource):
    @transactions_ns.expect(get_transaction_query_parser)
    @transactions_ns.doc(description="Get the transactions data")
    @transactions_ns.response(
        HTTPStatus.OK, "Success", model=TransactionsContent.get_api_model(transactions_ns)
    )
    def get(self):
        queries = get_transaction_query_parser.parse_args()
        page = queries["page"]
        search = queries["search"]
        category = queries["category"]
        sortBy = queries["sortBy"]

        transactions_content = get_transactions(page, search, category, sortBy)

        return jsonify(transactions_content.model_dump())


transactions_ns.add_resource(TransactionsApi, "")
