from enums.subscriptions.subscription_status_enum import SubscriptionStatus
from models.subscriptions_model import RecurringBillsSummary, Subscription
from schemas.subscription_schema import Subscription as SubscriptionSchema


def get_recurring_bills_summary():
    SubscriptionSchema.query.filter(SubscriptionSchema.is_deleted == False)
    return RecurringBillsSummary(
        paidAmount=190, totalUpcomingAmount=194.98, dueSoonAmount=59.98
    )


def get_subscriptions():
    return [
        Subscription(
            amount=subscription.amount,
            avatarUrl=subscription.avatar_url,
            user=subscription.user,
            recurrence=subscription.recurrence,
            startDate=subscription.start_date,
            status=subscription.status,
        )
        for subscription in SubscriptionSchema.query.filter(
            SubscriptionSchema.is_deleted == False,
            SubscriptionSchema.status == SubscriptionStatus.Inactive,
        ).all()
    ]
