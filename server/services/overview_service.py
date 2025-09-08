from models.overview_model import Balance, OverviewContent
from services.subscriptions_service import get_recurring_bills_monthly_summary
from services.transactions_service import get_overview_transactions
from services.budgets_service import get_overview_budgets
from services.pots_service import get_overview_pots


def get_overview():
    balance = Balance(current=4836.00, income=3814.25, expenses=1700.50)
    pots = get_overview_pots()
    budgets = get_overview_budgets()
    transactions = get_overview_transactions()
    recurringBillsSummary = get_recurring_bills_monthly_summary()
    summary = OverviewContent(
        balance=balance,
        pots=pots,
        budgets=budgets,
        transactions=transactions,
        recurringBillsSummary=recurringBillsSummary,
    )
    return summary
