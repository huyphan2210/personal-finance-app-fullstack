from sqlalchemy import func
from database import db
from enums.color_enum import Color
from models.budgets_model import Budget, BudgetOverviewContent
from schemas.budgets_schema import Budget as BudgetSchema


def get_overview_budgets():
    total_spent, total_maximum = [
        value or 0
        for value in db.session.query(
            func.sum(BudgetSchema.spent), func.sum(BudgetSchema.maximum)
        ).one()
    ]

    representBudgets = BudgetSchema.query.filter_by(is_deleted=False).order_by(
        BudgetSchema.category
    )

    return BudgetOverviewContent(
        totalSpent=total_spent,
        totalMaximum=total_maximum,
        representBudgets=[
            Budget(
                category=budget.category,
                maximum=budget.maximum,
                colorTheme=(
                    budget.color_theme
                    if budget.color_theme in Color.__members__.values()
                    else "#000"
                ),
            )
            for budget in representBudgets
        ],
    )
