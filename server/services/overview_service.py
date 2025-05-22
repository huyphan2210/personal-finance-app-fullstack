from models.overview_model import Balance, OverviewContent
from services.transactions_serivce import get_overview_transactions
from services.budgets_service import get_budgets
from services.pots_service import get_pots


def get_overview():
    balance = Balance(current=4836.00, income=3814.25, expenses=1700.50)
    pots = get_pots()
    budgets = get_budgets()
    transactions = get_overview_transactions()
    summary = OverviewContent(
        balance=balance, pots=pots, budgets=budgets, transactions=transactions
    )
    return summary
