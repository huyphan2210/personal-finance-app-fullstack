from models.base_model import BaseModel
from models.pots_model import Pot
from models.budgets_model import Budget, BudgetOverviewContent
from models.transactions_model import Transaction
from models.recurring_bills_model import RecurringBillsSummary


class Balance(BaseModel):
    current: float
    income: float
    expenses: float


class OverviewContent(BaseModel):
    balance: Balance
    pots: list[Pot]
    budgets: BudgetOverviewContent
    transactions: list[Transaction]
    recurringBillsSummary: RecurringBillsSummary
