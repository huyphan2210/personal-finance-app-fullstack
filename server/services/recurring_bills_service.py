from models.recurring_bills_model import RecurringBillsSummary


def get_recurring_bills_summary():
    return RecurringBillsSummary(
        paidAmount=190, totalUpcomingAmount=194.98, dueSoonAmount=59.98
    )
