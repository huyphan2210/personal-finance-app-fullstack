from flask import jsonify
from flask_restx import Namespace, Resource

from services.budgets_service import get_budgets
from models.budgets_model import BudgetContent

BUGDGETS = "budgets-api"
budgets_ns = Namespace(f"{BUGDGETS}", description="Get Budgets content")


class BudgetsApi(Resource):
    @budgets_ns.doc(description="Get the budgets data")
    @budgets_ns.response(200, "Success", model=BudgetContent.get_api_model(budgets_ns))
    def get(self):
        budgets = get_budgets()
        return jsonify(budgets.model_dump())


budgets_ns.add_resource(BudgetsApi, "")
