from models.transactions_model import Transaction
from services.transactions_service import IMAGE_HOSTING_URI
from sqlalchemy import func, desc
from database import db
from enums.color_enum import Color
from models.budgets_model import Budget, BudgetContent
from schemas.budget_schema import Budget as BudgetSchema
from schemas.transaction_schema import Transaction as TransactionSchema


def get_overview_budgets():
    total_spent, total_maximum = [
        value or 0
        for value in db.session.query(
            func.sum(BudgetSchema.spent), func.sum(BudgetSchema.maximum)
        ).one()
    ]

    representBudgets = (
        BudgetSchema.query.filter_by(is_deleted=False)
        .order_by(BudgetSchema.category)
        .limit(4)
    )

    return BudgetContent(
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
                spent=budget.spent,
            )
            for budget in representBudgets
        ],
    )


def get_budgets():
    total_spent, total_maximum = [
        value or 0
        for value in db.session.query(
            func.sum(BudgetSchema.spent), func.sum(BudgetSchema.maximum)
        ).one()
    ]

    representBudgets = BudgetSchema.query.filter_by(is_deleted=False).order_by(
        BudgetSchema.category
    )

    return BudgetContent(
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
                spent=budget.spent,
                representTransactions=[
                    Transaction(
                        avatarUrl=IMAGE_HOSTING_URI + transaction.avatar_url,
                        user=transaction.user,
                        category=transaction.category,
                        date=transaction.date,
                        amount=transaction.amount,
                        recurring=transaction.recurring,
                    )
                    for transaction in (
                        TransactionSchema.query.filter(
                            TransactionSchema.is_deleted == False,
                            TransactionSchema.category == budget.category,
                        )
                        .order_by(desc(TransactionSchema.created_at))
                        .limit(3)
                        .all()
                    )
                ],
            )
            for budget in representBudgets
        ],
    )
