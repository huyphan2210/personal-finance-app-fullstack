from datetime import datetime
from models.transactions_model import Transaction
from models.category_model import Category


def get_overview_transactions():
    overview_transactions: list[Transaction] = [
        Transaction(
            avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
            user="Emma Richardson",
            category=Category.General,
            date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
            amount=75.5,
            recurring=False,
        ),
        Transaction(
            avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793083/savory-bites-bistro_ha4gab.jpg",
            user="Savory Bites Bistro",
            category=Category.DiningOut,
            date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
            amount=-55.5,
            recurring=False,
        ),
        Transaction(
            avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793081/daniel-carter_nebsvx.jpg",
            user="Daniel Carter",
            category=Category.General,
            date=datetime.fromisoformat("2024-08-18T09:45:32+00:00"),
            amount=-42.3,
            recurring=False,
        ),
        Transaction(
            avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793084/sun-park_zsh0wa.jpg",
            user="Sun Park",
            category=Category.General,
            date=datetime.fromisoformat("2024-08-17T16:12:05+00:00"),
            amount=120.0,
            recurring=False,
        ),
        Transaction(
            avatarUrl="https://res.cloudinary.com/dejteftxn/image/upload/v1747793085/urban-services-hub_bclams.jpg",
            user="Urban Services Hub",
            category=Category.General,
            date=datetime.fromisoformat("2024-08-17T21:08:09+00:00"),
            amount=-65.0,
            recurring=False,
        ),
    ]

    return overview_transactions
