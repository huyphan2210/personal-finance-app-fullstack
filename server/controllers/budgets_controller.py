import uuid
from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

from enums.category_enum import Category
from enums.color_enum import Color
from exceptions import BadRequestError, NotFoundError
from services.budgets_service import (
    get_budgets,
    create_budget,
    update_budget,
    delete_budget,
)
from models.budgets_model import (
    BudgetContent,
    CreateBudgetDto,
    UpdateBudgetDto,
    DeleteBudgetDto,
)

BUGDGETS = "budgets-api"
budgets_ns = Namespace(f"{BUGDGETS}", description="Get Budgets content")

budget_dto = {
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
}

delete_budget_dto = {
    "id": fields.String(
        required=True,
        description="Budget ID (UUID)"
    )
}

update_budget_dto = {
    **budget_dto,
    **delete_budget_dto
}

create_budget_model = budgets_ns.model("CreateBudget", budget_dto)
update_budget_model = budgets_ns.model("UpdateBudget", update_budget_dto)
delete_budget_model = budgets_ns.model("DeleteBudget", delete_budget_dto)


@budgets_ns.response(HTTPStatus.INTERNAL_SERVER_ERROR, "Internal Server Error")
class BudgetsApi(Resource):
    @budgets_ns.doc(description="Get the budgets data")
    @budgets_ns.response(
        HTTPStatus.OK, "Success", model=BudgetContent.get_api_model(budgets_ns)
    )
    def get(self):
        budgets = get_budgets()
        return jsonify(budgets.model_dump())

    @budgets_ns.doc(description="Create new budget")
    @budgets_ns.expect(create_budget_model)
    @budgets_ns.response(HTTPStatus.CREATED, "Created")
    @budgets_ns.response(HTTPStatus.BAD_REQUEST, "Invalid input")
    def post(self):
        requestBody = request.get_json()
        try:
            try:
                create_budget_dto = CreateBudgetDto(**requestBody)
            except ValueError as e:
                raise BadRequestError(str(e))
            create_budget(create_budget_dto)
        except BadRequestError as e:
            return e.args[0], HTTPStatus.BAD_REQUEST

        return "Created", HTTPStatus.CREATED

    @budgets_ns.doc(description="Edit budget")
    @budgets_ns.expect(update_budget_model)
    @budgets_ns.response(HTTPStatus.OK, "Updated")
    @budgets_ns.response(HTTPStatus.BAD_REQUEST, "Invalid Request Body")
    @budgets_ns.response(HTTPStatus.NOT_FOUND, "Budget Not Found")
    def patch(self):
        requestBody = request.get_json()
        try:
            try:
                update_budget_model = UpdateBudgetDto(**requestBody)
            except ValueError as e:
                raise BadRequestError(str(e))
            update_budget(update_budget_model)
        except BadRequestError as e:
            return e.args[0], HTTPStatus.BAD_REQUEST
        except NotFoundError as e:
            return e.args[0], HTTPStatus.NOT_FOUND

        return "Updated", HTTPStatus.OK

    @budgets_ns.doc(description="Delete budget")
    @budgets_ns.expect(delete_budget_model)
    @budgets_ns.response(HTTPStatus.OK, "Deleted")
    @budgets_ns.response(HTTPStatus.BAD_REQUEST, "Invalid Request Body")
    @budgets_ns.response(HTTPStatus.NOT_FOUND, "Budget Not Found")
    def delete(self):
        requestBody = request.get_json()
        try:
            try:
                delete_budget_model = DeleteBudgetDto(**requestBody)
            except ValueError as e:
                raise BadRequestError(str(e))
            delete_budget(delete_budget_model)
        except BadRequestError as e:
            return e.args[0], HTTPStatus.BAD_REQUEST
        except NotFoundError as e:
            return e.args[0], HTTPStatus.NOT_FOUND

        return "Deleted", HTTPStatus.OK


budgets_ns.add_resource(BudgetsApi, "")
