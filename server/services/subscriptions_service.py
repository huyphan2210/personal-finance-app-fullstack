from sqlalchemy import desc

from enums.subscriptions.subscription_status_enum import SubscriptionStatus
from exceptions import BadRequestError
from models.subscriptions_model import RecurringBillsSummary, Subscription
from schemas.subscription_schema import Subscription as SubscriptionSchema
from utilities import IMAGE_HOSTING_URI

SUBSCRIPTIONS_PER_PAGE = 10

SORT_OPTIONS = {
    "Latest": desc(SubscriptionSchema.start_date),
    "Oldest": SubscriptionSchema.start_date,
    "A to Z": SubscriptionSchema.user,
    "Z to A": desc(SubscriptionSchema.user),
    "Highest": desc(SubscriptionSchema.amount),
    "Lowest": SubscriptionSchema.amount,
}


def get_recurring_bills_summary():
    SubscriptionSchema.query.filter(SubscriptionSchema.is_deleted == False)
    return RecurringBillsSummary(
        paidAmount=190, totalUpcomingAmount=194.98, dueSoonAmount=59.98
    )


def validate_get_subscriptions(
    page: int, search_string: str, sort_by: str
):
    # Validate page
    if page <= 0:
        raise BadRequestError("Page number must be positive.")

    # Validate search string
    if search_string and not isinstance(search_string, str):
        raise BadRequestError("Your search is not a string.")
    if len(search_string) > 50:
        raise BadRequestError("Your search is too long.")

    # Validate sortBy
    if sort_by not in SORT_OPTIONS.keys():
        raise BadRequestError("Sort is not approriate.")


def get_subscriptions(page: int, search_string: str, sort_by: str):
    validate_get_subscriptions(page, search_string, sort_by)
    return [
        Subscription(
            amount=subscription.amount,
            avatarUrl=IMAGE_HOSTING_URI + subscription.avatar_url,
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
