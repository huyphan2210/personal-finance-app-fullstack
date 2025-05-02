from pydantic import BaseModel
from flask_restx import fields, Api


class Balance(BaseModel):
    current: float
    income: float
    expenses: float

    def get_api_model(api):
        return api.model(
            Balance.__name__,
            {
                "current": fields.Float(required=True, description="Current balance"),
                "income": fields.Float(required=True, description="Total income"),
                "expenses": fields.Float(required=True, description="Total expenses"),
            },
        )


class OverviewSummary(BaseModel):
    balance: Balance

    def get_api_model(api: Api):
        return api.model(
            OverviewSummary.__name__,
            {
                "balance": fields.Nested(Balance.get_api_model(api)),
            },
        )
