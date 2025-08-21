from http import HTTPStatus
from flask import jsonify
from flask_restx import Namespace, Resource

from services.pots_service import get_pots
from models.pots_model import Pots

POTS = "pots-api"
pots_ns = Namespace(f"{POTS}", description="Get Pots content")


class PotsApi(Resource):
    @pots_ns.doc(description="Get the pots data")
    @pots_ns.response(HTTPStatus.OK, "Success", model=Pots.get_api_model(pots_ns))
    def get(self):
        pots = get_pots()
        return jsonify(pots.model_dump())


pots_ns.add_resource(PotsApi, "")
