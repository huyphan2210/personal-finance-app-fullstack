from models.overview_model import Balance, OverviewContent


def get_overview():
    balance = Balance(current=4836.00, income=3814.25, expenses=1700.50)
    summary = OverviewContent(balance=balance)
    return summary
