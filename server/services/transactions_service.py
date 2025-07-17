import os
from sqlalchemy import String, cast, desc, or_
from sqlalchemy.orm import Query
from exceptions import BadRequestError

from models.transactions_model import Transaction, TransactionsContent
from enums.category_enum import Category
from schemas.transaction_schema import Transaction as TransactionSchema

IMAGE_HOSTING_URI = os.getenv(
    "IMAGE_HOSTING_URI", "https://res.cloudinary.com/dejteftxn/image/upload/"
)
TRANSACTIONS_PER_PAGE = 10

SORT_OPTIONS = {
    "Latest": desc(TransactionSchema.date),
    "Oldest": TransactionSchema.date,
    "A to Z": TransactionSchema.user,
    "Z to A": desc(TransactionSchema.user),
    "Highest": desc(TransactionSchema.amount),
    "Lowest": TransactionSchema.amount,
}


def get_overview_transactions():
    transactions: list[TransactionSchema] = (
        TransactionSchema.query.filter_by(is_deleted=False)
        .order_by(desc(TransactionSchema.date))
        .limit(5)
    )

    overview_transactions = [
        Transaction(
            avatarUrl=IMAGE_HOSTING_URI + transaction.avatar_url,
            user=transaction.user,
            category=transaction.category,
            date=transaction.date,
            amount=transaction.amount,
            recurring=transaction.recurring,
        )
        for transaction in transactions
    ]

    return overview_transactions


def get_transactions(page: int, search_string: str, category: str, sort_by: str):
    validate_get_transactions(page, search_string, category, sort_by)

    transaction_query = transform_transaction_query(search_string, category, sort_by)

    transactions: list[TransactionSchema] = transaction_query.limit(
        TRANSACTIONS_PER_PAGE
    ).offset((page - 1) * TRANSACTIONS_PER_PAGE)

    totalRows = transaction_query.count()
    numberOfPages = totalRows // TRANSACTIONS_PER_PAGE
    if totalRows > TRANSACTIONS_PER_PAGE and totalRows % TRANSACTIONS_PER_PAGE > 0:
        numberOfPages += 1

    return TransactionsContent(
        transactions=[
            Transaction(
                avatarUrl=IMAGE_HOSTING_URI + transaction.avatar_url,
                user=transaction.user,
                category=transaction.category,
                date=transaction.date,
                amount=transaction.amount,
                recurring=transaction.recurring,
            )
            for transaction in transactions
        ],
        numberOfPages=numberOfPages,
        currentPage=page,
    )


def validate_get_transactions(
    page: int, search_string: str, category: str, sort_by: str
):
    # Validate page
    if page <= 0:
        raise BadRequestError("Page number must be positive.")

    # Validate category
    if category and category not in Category.__members__.values():
        raise BadRequestError(f"Category {category} doesn't exist. ")

    # Validate search string
    if search_string and not isinstance(search_string, str):
        raise BadRequestError("Your search is not a string.")
    if len(search_string) > 50:
        raise BadRequestError("Your search is too long.")

    # Validate sortBy
    if sort_by not in SORT_OPTIONS.keys():
        raise BadRequestError("Sort is not approriate.")


def transform_transaction_query(search_string: str, category: str, sort_by: str):
    transaction_query = TransactionSchema.query.filter_by(is_deleted=False)
    for filter_fn in [
        lambda query: filter_transactions_by_search(query, search_string),
        lambda query: filter_transactions_by_category(query, category),
        lambda query: filter_transactions_with_sort_by(query, sort_by),
    ]:
        transaction_query = filter_fn(transaction_query)

    return transaction_query


def filter_transactions_by_search(transaction_query: Query, search_string: str):
    if search_string:
        search = f"%{search_string}%"
        try:
            search_amount = f"%{int(search_string)}%"
        except ValueError:
            try:
                search_amount = f"%{float(search_string)}%"
            except ValueError:
                search_amount = ""

        transaction_query = transaction_query.filter(
            or_(
                TransactionSchema.user.ilike(search),
                cast(TransactionSchema.amount, String).ilike(search_amount),
            )
        )

    return transaction_query


def filter_transactions_by_category(transaction_query: Query, category: str):
    if category:
        transaction_query = transaction_query.filter(
            TransactionSchema.category == category
        )

    return transaction_query


def filter_transactions_with_sort_by(transaction_query: Query, sort_by: str):
    sort_clause = SORT_OPTIONS.get(sort_by)
    if sort_clause is not None:
        transaction_query = transaction_query.order_by(sort_clause)

    return transaction_query
