from flask_restx import fields, Api
from models.base_model import BaseModel


class Balance(BaseModel):
    current: float
    income: float
    expenses: float


class OverviewContent(BaseModel):
    balance: Balance
