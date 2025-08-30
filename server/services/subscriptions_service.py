from models.recurring_bills_model import RecurringBillsSummary
from schemas.subscription_schema import Subscription as SubscriptionSchema

def get_recurring_bills_summary():
    SubscriptionSchema.query.filter(SubscriptionSchema.is_deleted==False)
    return RecurringBillsSummary(
        paidAmount=190, totalUpcomingAmount=194.98, dueSoonAmount=59.98
    )
