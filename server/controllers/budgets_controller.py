from flask import jsonify, request
from flask_restx import Namespace, Resource, fields

from enums.category_enum import Category
from enums.color_enum import Color
from exceptions import BadRequestError
from services.budgets_service import get_budgets, create_budget
from models.budgets_model import BudgetContent, CreateBudgetDto

BUGDGETS = "budgets-api"
budgets_ns = Namespace(f"{BUGDGETS}", description="Get Budgets content")

# Define your Swagger model (mirrors CreateBudgetDto)
create_budget_model = budgets_ns.model(
    "CreateBudget",
    {
        "category": fields.String(
            required=True,
            description="Budget category",
            enum=[e.value for e in Category],
        ),
        "colorTheme": fields.String(
            required=True,
            description="Budget color theme",
            enum=[e.value for e in Color],
        ),
        "maximum": fields.Float(required=True, description="Maximum allowed budget"),
    },
)


@budgets_ns.response(500, "Internal Server Error")
class BudgetsApi(Resource):
    @budgets_ns.doc(description="Get the budgets data")
    @budgets_ns.response(200, "Success", model=BudgetContent.get_api_model(budgets_ns))
    def get(self):
        budgets = get_budgets()
        return jsonify(budgets.model_dump())

    @budgets_ns.doc(description="Create new budget")
    @budgets_ns.expect(create_budget_model)
    @budgets_ns.response(201, "Created")
    @budgets_ns.response(400, "Invalid input")
    def post(self):
        requestBody = request.get_json()

        try:
            create_budget_dto = CreateBudgetDto(**requestBody)
        except ValueError as e:
            raise BadRequestError(str(e))

        create_budget(create_budget_dto)
        return jsonify("Created", 201)


budgets_ns.add_resource(BudgetsApi, "")
