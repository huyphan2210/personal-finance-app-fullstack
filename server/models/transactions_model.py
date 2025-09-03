from datetime import datetime
from typing import Optional
from uuid import UUID
from enums.category_enum import Category
from models.base_model import BaseModel


class Transaction(BaseModel):
    avatarUrl: str
    user: str
    category: Category
    date: datetime
    amount: float
    subscriptionId: Optional[UUID] = None


class TransactionsContent(BaseModel):
    transactions: list[Transaction]
    numberOfPages: int
    currentPage: int
