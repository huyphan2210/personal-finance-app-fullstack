from flask import Blueprint
from flask_restx import Api, Resource
from services.overview_service import get_overview

from models.overview_model import OverviewContent

OVERVIEW = "overview"
overview_bp = Blueprint("OVERVIEW", __name__)
overview_api = Api(overview_bp)
overview_ns = overview_api.namespace(
    f"{OVERVIEW}", description="Get summary of Overview"
)


class Overview(Resource):
    @overview_ns.marshal_with(OverviewContent.get_api_model(overview_api))
    def get(self):
        overview_content = get_overview()
        return overview_content.dict()


overview_ns.add_resource(Overview, "")
