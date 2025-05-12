from flask_restx import Namespace, Resource

from services.overview_service import get_overview
from models.overview_model import OverviewContent

OVERVIEW = "overview"
overview_ns = Namespace(f"{OVERVIEW}", description="Get summary of Overview")


class Overview(Resource):
    @overview_ns.marshal_with(OverviewContent.get_api_model(overview_ns))
    def get(self):
        overview_content = get_overview()
        return overview_content.dict()


overview_ns.add_resource(Overview, "")
