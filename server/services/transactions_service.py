import os
from datetime import datetime
from sqlalchemy import desc
from exceptions import BadRequestError, NotFoundError

from models.transactions_model import Transaction, TransactionsContent
from models.category_model import Category
from schemas.transactions_schema import Transaction as TransactionSchema

IMAGE_HOSTING_URI = os.getenv(
    "IMAGE_HOSTING_URI", "https://res.cloudinary.com/dejteftxn/image/upload/"
)
TRANSACTIONS_PER_PAGE = 10


def get_overview_transactions():
    transactions: list[TransactionSchema] = TransactionSchema.query.order_by(
        desc(TransactionSchema.date)
    ).limit(5)

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
    transaction_query = TransactionSchema.query

    if search_string:
        search = f"%{search_string}%"
        transaction_query = transaction_query.filter(
            TransactionSchema.user.ilike(search)
        )

    if category:
        transaction_query = transaction_query.filter(
            TransactionSchema.category == category
        )

    transactions: list[TransactionSchema] = transaction_query.limit(
        TRANSACTIONS_PER_PAGE
    ).offset(page - 1)

    # transactions = [
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
    #         user="Emma Richardson",
    #         category=Category.General,
    #         date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
    #         amount=75.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793083/savory-bites-bistro_ha4gab.jpg",
    #         user="Savory Bites Bistro",
    #         category=Category.DiningOut,
    #         date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
    #         amount=-55.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
    #         user="Emma Richardson",
    #         category=Category.General,
    #         date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
    #         amount=75.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793083/savory-bites-bistro_ha4gab.jpg",
    #         user="Savory Bites Bistro",
    #         category=Category.DiningOut,
    #         date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
    #         amount=-55.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
    #         user="Emma Richardson",
    #         category=Category.General,
    #         date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
    #         amount=75.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793083/savory-bites-bistro_ha4gab.jpg",
    #         user="Savory Bites Bistro",
    #         category=Category.DiningOut,
    #         date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
    #         amount=-55.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
    #         user="Emma Richardson",
    #         category=Category.General,
    #         date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
    #         amount=75.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793083/savory-bites-bistro_ha4gab.jpg",
    #         user="Savory Bites Bistro",
    #         category=Category.DiningOut,
    #         date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
    #         amount=-55.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
    #         user="Emma Richardson",
    #         category=Category.General,
    #         date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
    #         amount=75.5,
    #         recurring=False,
    #     ),
    #     Transaction(
    #         avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793083/savory-bites-bistro_ha4gab.jpg",
    #         user="Savory Bites Bistro",
    #         category=Category.DiningOut,
    #         date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
    #         amount=-55.5,
    #         recurring=False,
    #     ),
    # ]

    totalRows = transaction_query.count()
    numberOfPages = totalRows // TRANSACTIONS_PER_PAGE
    if totalRows % TRANSACTIONS_PER_PAGE > 0:
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
    )


def validate_get_transactions(
    page: int, search_string: str, category: str, sort_by: str
):
    # Validate page
    if page <= 0:
        raise BadRequestError("Page number must be positive.")

    # Validate category
    if category and category not in Category.__members__:
        raise BadRequestError(f"Category {category} doesn't exist. ")

    # Validate search string
    if search_string and not isinstance(search_string, str):
        raise BadRequestError("Your search is not a string.")
    if len(search_string) > 50:
        raise BadRequestError("Your search is too long.")

    # Validate sortBy
    if sort_by not in [
        "Latest",
        "Oldest",
        "A to Z",
        "Z to A",
        "Highest",
        "Lowest",
    ]:
        raise BadRequestError("Sort is not approriate.")
