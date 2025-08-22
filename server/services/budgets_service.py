from uuid import UUID
from models.transactions_model import Transaction
from services.transactions_service import IMAGE_HOSTING_URI
from sqlalchemy import func, desc, or_
from database import db
from enums.color_enum import Color
from models.budgets_model import (
    Budget,
    BudgetContent,
    CreateBudgetDto,
    UpdateBudgetDto,
    DeleteBudgetDto,
)
from schemas.budget_schema import Budget as BudgetSchema
from schemas.transaction_schema import Transaction as TransactionSchema
from exceptions import BadRequestError, NotFoundError


def get_overview_budgets():
    total_spent, total_maximum = [
        value or 0
        for value in db.session.query(
            func.sum(BudgetSchema.spent), func.sum(BudgetSchema.maximum)
        )
        .filter(BudgetSchema.is_deleted == False)
        .one()
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
                    budget.color_theme.lower()
                    if budget.color_theme.lower() in {c.value.lower() for c in Color}
                    else "#000"
                ),
                spent=budget.spent,
                representTransactions=[],
            )
            for budget in representBudgets
        ],
    )


def get_budgets():
    total_spent, total_maximum = [
        value or 0
        for value in db.session.query(
            func.sum(BudgetSchema.spent), func.sum(BudgetSchema.maximum)
        )
        .filter(BudgetSchema.is_deleted == False)
        .one()
    ]

    representBudgets = BudgetSchema.query.filter_by(is_deleted=False).order_by(
        BudgetSchema.category
    )

    return BudgetContent(
        totalSpent=total_spent,
        totalMaximum=total_maximum,
        representBudgets=[
            Budget(
                id=budget.id,
                category=budget.category,
                maximum=budget.maximum,
                colorTheme=(
                    budget.color_theme.lower()
                    if budget.color_theme.lower() in {c.value.lower() for c in Color}
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
                            TransactionSchema.amount < 0,
                        )
                        .order_by(desc(TransactionSchema.date))
                        .limit(3)
                        .all()
                    )
                ],
            )
            for budget in representBudgets
        ],
    )


def validate_budget_dto(create_budget_dto: CreateBudgetDto):
    existing_budget = (
        BudgetSchema.query.filter(
            BudgetSchema.is_deleted == False,
            or_(
                BudgetSchema.category == create_budget_dto.category,
                BudgetSchema.color_theme == create_budget_dto.colorTheme.value.lower(),
            ),
        )
        .limit(1)
        .one_or_none()
    )

    if (
        existing_budget is not None
        and existing_budget.category == create_budget_dto.category
    ):
        raise BadRequestError("The category existed.")
    elif (
        existing_budget is not None
        and existing_budget.color_theme.lower() == create_budget_dto.colorTheme.lower()
    ):
        raise BadRequestError("The color has been used.")

    if create_budget_dto.maximum <= 0:
        raise BadRequestError("Maximum of the budget must be positive.")


def create_budget(create_budget_dto: CreateBudgetDto):
    validate_budget_dto(create_budget_dto)
    new_budget = BudgetSchema(
        category=create_budget_dto.category,
        maximum=create_budget_dto.maximum,
        color_theme=create_budget_dto.colorTheme.lower(),
        spent=0,
    )
    db.session.add(new_budget)
    db.session.commit()
    return new_budget


def update_budget(update_budget_dto: UpdateBudgetDto):
    existing_budget = (
        BudgetSchema.query.filter(
            BudgetSchema.id == update_budget_dto.id,
            BudgetSchema.is_deleted == False,
        )
        .limit(1)
        .one_or_none()
    )

    if existing_budget is None:
        raise NotFoundError("The budget doesn't exist")

    existing_budget.maximum = update_budget_dto.maximum
    existing_budget.category = update_budget_dto.category
    existing_budget.color_theme = update_budget_dto.colorTheme.lower()
    db.session.commit()

    return


def delete_budget(budget_id: UUID):
    existing_budget = (
        BudgetSchema.query.filter(
            BudgetSchema.id == budget_id,
            BudgetSchema.is_deleted == False,
        )
        .limit(1)
        .one_or_none()
    )

    if existing_budget is None:
        raise NotFoundError("The budget doesn't exist")

    existing_budget.is_deleted = True
    db.session.commit()

    return
