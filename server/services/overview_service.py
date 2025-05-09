from models.overview_model import Balance, OverviewContent
from services.pots_service import get_pots


def get_overview():
    balance = Balance(current=4836.00, income=3814.25, expenses=1700.50)
    pots = get_pots()
    summary = OverviewContent(balance=balance, pots=pots)
    return summary
