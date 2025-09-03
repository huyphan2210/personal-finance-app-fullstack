from http import HTTPStatus
from flask import jsonify
from flask_restx import Namespace, Resource, reqparse

from services.subscriptions_service import get_subscriptions
from models.subscriptions_model import Subscription

SUBSCRIPTIONS = "subscriptions-api"
subscriptions_ns = Namespace(f"{SUBSCRIPTIONS}", description="Get subscription content")

get_subscription_query_parser = reqparse.RequestParser()
get_subscription_query_parser.add_argument("page", type=int, default=1)
get_subscription_query_parser.add_argument("search", type=str, default="")
get_subscription_query_parser.add_argument("sortBy", type=str, default="")


class SubscriptionsApi(Resource):
    @subscriptions_ns.expect(get_subscription_query_parser)
    @subscriptions_ns.doc(description="Get the transactions data")
    @subscriptions_ns.response(
        HTTPStatus.OK, "Success", model=Subscription.get_api_model(subscriptions_ns)
    )
    def get(self):
        queries = get_subscription_query_parser.parse_args()
        page = queries["page"]
        search = queries["search"]
        sort_by = queries["sortBy"]

        subscriptions = get_subscriptions(page, search, sort_by)

        return jsonify(subscriptions.model_dump())


subscriptions_ns.add_resource(SubscriptionsApi, "")
