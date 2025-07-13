from enums.color_enum import Color
from models.base_model import BaseModel
from enums.category_enum import Category


class Budget(BaseModel):
    maximum: float
    spent: float
    category: Category
    colorTheme: Color


class BudgetContent(BaseModel):
    totalSpent: float
    totalMaximum: float
    representBudgets: list[Budget]
