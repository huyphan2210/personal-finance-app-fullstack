from flask import Blueprint
from flask_restx import Api

from controllers.overview_controller import overview_ns
from controllers.pots_controller import pots_ns

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp, title="My API", version="1.0")

api.add_namespace(overview_ns)
api.add_namespace(pots_ns)
