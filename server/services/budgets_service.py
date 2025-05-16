from models.budgets_model import Budget
from models.category_model import Category


def get_budgets():
    budgets: list[Budget] = [
        Budget(category=Category.Entertainment, maximum=50),
        Budget(category=Category.Bills, maximum=750),
        Budget(category=Category.DiningOut, maximum=75),
        Budget(category=Category.PersonalCare, maximum=100),
    ]
    return budgets
