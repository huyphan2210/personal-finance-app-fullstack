from flask import Blueprint, jsonify
from flask_restx import Api, Resource, fields
from services.pots_service import get_pots
from models.pots_model import Pots

POTS = "pots"
pots_bp = Blueprint(POTS.upper(), __name__)
pots_api = Api(pots_bp)
pots_ns = pots_api.namespace(f"{POTS}", description="Get Pots content")


class Pots(Resource):
    @pots_ns.marshal_with(Pots.get_api_model(pots_api))
    def get(self):
        pots = get_pots()
        return Pots(pots=pots).dict()


pots_ns.add_resource(Pots, "")
