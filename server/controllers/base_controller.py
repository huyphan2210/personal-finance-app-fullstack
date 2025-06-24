from flask import Blueprint
from flask_restx import Api

from controllers.overview_controller import overview_ns
from controllers.transactions_controller import transactions_ns
from controllers.pots_controller import pots_ns
from enums.category_enum import Category
from enums.color_enum import Color

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp, title="My API", version="1.0")

api.add_namespace(overview_ns)
api.add_namespace(transactions_ns)
api.add_namespace(pots_ns)


@api.documentation
def custom_spec_for_enum():
    # from flask import jsonify

    spec = api.__schema__

    # Look for the schema that has your enum
    for definition in spec.get("definitions", {}).values():
        for props in definition.get("properties", {}).values():
            if props.get("enum") == [e.value for e in Color]:
                props["x-enum-varnames"] = list(Color.__members__.keys())
            if props.get("enum") == [e.value for e in Category]:
                props["x-enum-varnames"] = list(Category.__members__.keys())

    return spec
