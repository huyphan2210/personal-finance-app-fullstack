from collections import defaultdict
from datetime import datetime, timezone
from uuid import UUID
from sqlalchemy import desc, func, or_, String, cast
from sqlalchemy.orm import Query
from database import db

from enums.subscriptions.subscription_recurrence_enum import SubscriptionRecurrence
from enums.subscriptions.subscription_status_enum import SubscriptionStatus
from exceptions import BadRequestError
from models.subscriptions_model import (
    RecurringBillsSummary,
    Subscription,
    SubscriptionsContent,
)
from schemas.subscription_schema import Subscription as SubscriptionSchema
from schemas.transaction_schema import Transaction as TransactionSchema

from utilities import IMAGE_HOSTING_URI

SUBSCRIPTIONS_PER_PAGE = 10

DUE_DAYS_MAX = 7

SORT_OPTIONS = {
    "Latest": desc(SubscriptionSchema.start_date),
    "Oldest": SubscriptionSchema.start_date,
    "A to Z": SubscriptionSchema.user,
    "Z to A": desc(SubscriptionSchema.user),
    "Highest": desc(SubscriptionSchema.amount),
    "Lowest": SubscriptionSchema.amount,
}


def get_recurring_bills_monthly_summary():
    paid_amount = 0
    total_upcoming_amount = 0
    due_soon_amount = 0

    monthly_subscriptions: list[SubscriptionSchema] = SubscriptionSchema.query.filter(
        SubscriptionSchema.is_deleted == False,
        SubscriptionSchema.status == SubscriptionStatus.Active,
        SubscriptionSchema.recurrence == SubscriptionRecurrence.Monthly,
    ).all()

    transactions: list[TransactionSchema] = (
        TransactionSchema.query.join(
            SubscriptionSchema,
            SubscriptionSchema.id == TransactionSchema.subscription_id,
        )
        .filter(
            TransactionSchema.is_deleted == False,
            SubscriptionSchema.is_deleted == False,
            SubscriptionSchema.status == SubscriptionStatus.Active,
            SubscriptionSchema.recurrence == SubscriptionRecurrence.Monthly,
            TransactionSchema.date <= SubscriptionSchema.next_due,
            (SubscriptionSchema.last_due == None)
            | (TransactionSchema.date >= SubscriptionSchema.last_due),
        )
        .all()
    )

    transactions_by_subscription: defaultdict[UUID, list[TransactionSchema]] = (
        defaultdict(list)
    )
    for transaction in transactions:
        transactions_by_subscription[transaction.subscription_id].append(transaction)

    for sub in monthly_subscriptions:
        transactions = transactions_by_subscription[sub.id]
        if sub.next_due.tzinfo is None:
            next_due = sub.next_due.replace(tzinfo=timezone.utc)
        else:
            next_due = sub.next_due

        if transactions and next_due:
            paid_amount += sum(transaction.amount for transaction in transactions)
        else:
            total_upcoming_amount += sub.amount

        if (next_due - datetime.now(timezone.utc)).days <= DUE_DAYS_MAX:
            due_soon_amount += sub.amount

    return RecurringBillsSummary(
        paidAmount=paid_amount,
        totalUpcomingAmount=total_upcoming_amount,
        dueSoonAmount=due_soon_amount,
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
    numberOfPages = max(
        1, (totalRows + SUBSCRIPTIONS_PER_PAGE - 1) // SUBSCRIPTIONS_PER_PAGE
    )

    total_monthly, total_yearly = [
        value or 0
        for value in db.session.query(
            func.sum(SubscriptionSchema.amount).filter(
                SubscriptionSchema.recurrence == SubscriptionRecurrence.Monthly
            ),
            func.sum(SubscriptionSchema.amount).filter(
                SubscriptionSchema.recurrence == SubscriptionRecurrence.Yearly
            ),
        )
        .filter(
            SubscriptionSchema.is_deleted == False,
            SubscriptionSchema.status == SubscriptionStatus.Active,
        )
        .one()
    ]

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
        monthlySummary=get_recurring_bills_monthly_summary(),
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
