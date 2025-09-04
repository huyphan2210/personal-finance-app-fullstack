from sqlalchemy import desc, or_, String, cast
from sqlalchemy.orm import Query

from enums.subscriptions.subscription_status_enum import SubscriptionStatus
from exceptions import BadRequestError
from models.subscriptions_model import (
    RecurringBillsSummary,
    Subscription,
    SubscriptionsContent,
)
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


def validate_get_subscriptions(page: int, search_string: str, sort_by: str):
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
    subscription_query = transform_subscription_query(page, search_string, sort_by)
    subscriptions: list[SubscriptionSchema] = subscription_query.limit(
        SUBSCRIPTIONS_PER_PAGE
    ).offset((page - 1) * SUBSCRIPTIONS_PER_PAGE)

    totalRows = subscription_query.count()
    numberOfPages = max(1, (totalRows + SUBSCRIPTIONS_PER_PAGE - 1) // SUBSCRIPTIONS_PER_PAGE)

    return SubscriptionsContent(
        subscriptions=[
            Subscription(
                avatarUrl=IMAGE_HOSTING_URI + subscription.avatar_url,
                user=subscription.user,
                dueDate=subscription.next_due,
                amount=subscription.amount,
                recurrence=subscription.recurrence,
                status=subscription.status,
            )
            for subscription in subscriptions
        ],
        numberOfPages=numberOfPages,
        currentPage=page,
    )


def transform_subscription_query(page: int, search_string: str, sort_by: str):
    subscription_query = SubscriptionSchema.query.filter(
        SubscriptionSchema.is_deleted == False,
        SubscriptionSchema.status == SubscriptionStatus.Active,
    )
    for filter_fn in [
        lambda query: filter_subscriptions_by_search(query, search_string),
        lambda query: filter_subscriptions_with_sort_by(query, sort_by),
    ]:
        subscription_query = filter_fn(subscription_query)

    return subscription_query


def filter_subscriptions_by_search(subscription_query: Query, search_string: str):
    if search_string:
        search = f"%{search_string}%"
        try:
            search_amount = f"%{int(search_string)}%"
        except ValueError:
            try:
                search_amount = f"%{float(search_string)}%"
            except ValueError:
                search_amount = ""

        subscription_query = subscription_query.filter(
            or_(
                SubscriptionSchema.user.ilike(search),
                cast(SubscriptionSchema.amount, String).ilike(search_amount),
            )
        )

    return subscription_query


def filter_subscriptions_with_sort_by(subscription_query: Query, sort_by: str):
    sort_clause = SORT_OPTIONS.get(sort_by)
    if sort_clause is not None:
        subscription_query = subscription_query.order_by(sort_clause)

    return subscription_query
