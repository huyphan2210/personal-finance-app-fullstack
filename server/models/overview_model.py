from flask_restx import fields, Api
from models.base_model import BaseModel
from models.pots_model import Pot
from models.budgets_model import Budget


class Balance(BaseModel):
    current: float
    income: float
    expenses: float


class OverviewContent(BaseModel):
    balance: Balance
    pots: list[Pot]
    budgets: list[Budget]
