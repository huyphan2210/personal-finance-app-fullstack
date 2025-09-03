from models.base_model import BaseModel
from models.pots_model import PotOverview
from models.budgets_model import BudgetContent
from models.transactions_model import Transaction
from models.subscriptions_model import RecurringBillsSummary


class Balance(BaseModel):
    current: float
    income: float
    expenses: float


class OverviewContent(BaseModel):
    balance: Balance
    pots: PotOverview
    budgets: BudgetContent
    transactions: list[Transaction]
    recurringBillsSummary: RecurringBillsSummary
