from flask_restx import Namespace, Resource

from services.pots_service import get_pots
from models.pots_model import Pots as PotsModel

POTS = "pots-api"
pots_ns = Namespace(f"{POTS}", description="Get Pots content")


class PotsApi(Resource):
    @pots_ns.marshal_with(PotsModel.get_api_model(pots_ns))
    def get(self):
        pots = get_pots()
        return PotsModel(pots=pots).dict()


pots_ns.add_resource(PotsApi, "")
