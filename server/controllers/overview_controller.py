from flask import jsonify
from flask_restx import Namespace, Resource

from services.overview_service import get_overview
from models.overview_model import OverviewContent

OVERVIEW = "overview-api"
overview_ns = Namespace(f"{OVERVIEW}", description="Get summary of Overview")


class OverviewApi(Resource):
    @overview_ns.doc(description="Get the overview data")
    @overview_ns.response(
        200, "Success", model=OverviewContent.get_api_model(overview_ns)
    )
    def get(self):
        overview_content = get_overview()
        return jsonify(overview_content.model_dump())


overview_ns.add_resource(OverviewApi, "")
