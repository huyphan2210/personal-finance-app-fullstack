from enums.color_enum import Color
from models.base_model import BaseModel
from enums.category_enum import Category
from models.transactions_model import Transaction


class Budget(BaseModel):
    maximum: float
    spent: float
    category: Category
    colorTheme: Color
    representTransactions: list[Transaction]


class BudgetContent(BaseModel):
    totalSpent: float
    totalMaximum: float
    representBudgets: list[Budget]


class CreateBudgetDto(BaseModel):
    category: Category
    colorTheme: Color
    maximum: float


class UpdateBudgetDto(BaseModel):
    category: Category
    colorTheme: Color
    maximum: float


class DeleteBudgetDto(BaseModel):
    category: Category
    colorTheme: Color
    maximum: float
