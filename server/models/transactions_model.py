from datetime import datetime
from models.category_model import Category
from models.base_model import BaseModel


class Transaction(BaseModel):
    avatarUrl: str
    user: str
    category: Category
    date: datetime
    amount: float
    recurring: bool


class TransactionsContent(BaseModel):
    transactions: list[Transaction]
    numberOfPages: int
    currentPage: int
