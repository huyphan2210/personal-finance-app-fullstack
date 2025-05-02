from flask import Blueprint
from flask_restx import Api, fields, Resource

from models.overview_model import OverviewSummary, Balance

OVERVIEW = "overview"
overview_bp = Blueprint("OVERVIEW", __name__)
overview_api = Api(overview_bp)
overview_ns = overview_api.namespace("", description="Get summary of Overview")


class OverviewApi(Resource):
    @overview_ns.marshal_with(OverviewSummary.get_api_model(overview_api))
    def get(self):
        balance = Balance(current=4836.00, income=3814.25, expenses=1700.50)
        summary = OverviewSummary(balance=balance)
        return summary.dict()


overview_ns.add_resource(OverviewApi, f"/{OVERVIEW}")
