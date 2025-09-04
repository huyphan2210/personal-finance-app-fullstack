from uuid import UUID
from database import db
from sqlalchemy import func, or_

from schemas.pot_schema import Pot as PotSchema
from models.pots_model import (
    CreatePotDto,
    DeletePotDto,
    Pot,
    PotOverview,
    Pots,
    UpdatePotDto,
)
from exceptions import BadRequestError, NotFoundError


def get_overview_pots():
    pots = PotSchema.query.filter_by(is_deleted=False).limit(4).all()
    total_saved = (
        db.session.query(func.sum(PotSchema.total)).filter_by(is_deleted=False).scalar()
        or 0
    )

    return PotOverview(
        pots=[
            Pot(
                id=str(pot.id),
                name=pot.name,
                target=pot.target,
                total=pot.total,
                colorTheme=pot.color_theme.lower(),
            )
            for pot in pots
        ],
        totalSaved=total_saved,
    )


def get_pots():
    pots = PotSchema.query.filter_by(is_deleted=False).all()
    return Pots(
        pots=[
            Pot(
                id=str(pot.id),
                name=pot.name,
                target=pot.target,
                total=pot.total,
                colorTheme=pot.color_theme.lower(),
            )
            for pot in pots
        ]
    )


def validate_create_pot_dto(create_pot_dto: CreatePotDto):
    if create_pot_dto.target <= 0:
        raise BadRequestError("The Pot's target must be a positive number.")

    if create_pot_dto.total is not None and create_pot_dto.total <= 0:
        raise BadRequestError("The Pot's total must be a positive number.")

    existing_pot = PotSchema.query.filter(
        or_(
            PotSchema.name == create_pot_dto.name,
            PotSchema.color_theme == create_pot_dto.colorTheme.value.lower(),
        ),
        PotSchema.is_deleted == False,
    ).one_or_none()

    if existing_pot is not None:
        raise BadRequestError("The Pot's name or color has been used.")


def validate_update_pot_dto(update_pot_dto: UpdatePotDto):
    if update_pot_dto.target is not None and update_pot_dto.target <= 0:
        raise BadRequestError("The Pot's target must be a positive number.")

    if update_pot_dto.total is not None and update_pot_dto.total < 0:
        raise BadRequestError("The Pot's total must be a >= 0.")

    if (
        update_pot_dto.total is not None
        and update_pot_dto.target is not None
        and update_pot_dto.total > update_pot_dto.target
    ):
        raise BadRequestError("The Pot's total must not exceed its target.")

    similar_pot = PotSchema.query.filter(
        or_(
            PotSchema.name == update_pot_dto.name,
            (
                PotSchema.color_theme == update_pot_dto.colorTheme.value.lower()
                if update_pot_dto.colorTheme is not None
                else None
            ),
        ),
        PotSchema.id != update_pot_dto.id,
        PotSchema.is_deleted == False,
    ).one_or_none()

    if similar_pot is not None:
        raise BadRequestError("The Pot's name or color has been used.")


def get_pot_with_id_or_raise(id: UUID):
    existing_pot = (
        PotSchema.query.filter(
            PotSchema.id == id,
            PotSchema.is_deleted == False,
        )
        .limit(1)
        .one_or_none()
    )

    if existing_pot is None:
        raise NotFoundError("The target Pot doesn't exist.")

    return existing_pot


def create_pot(create_pot_dto: CreatePotDto):
    validate_create_pot_dto(create_pot_dto)
    new_pot = PotSchema(
        name=create_pot_dto.name,
        target=create_pot_dto.target,
        color_theme=create_pot_dto.colorTheme.value.lower(),
        total=create_pot_dto.total or 0,
    )
    db.session.add(new_pot)
    db.session.commit()
    return new_pot


def update_pot(update_pot_dto: UpdatePotDto):
    validate_update_pot_dto(update_pot_dto)
    existing_pot = get_pot_with_id_or_raise(update_pot_dto.id)

    update_data = update_pot_dto.model_dump(exclude_none=True)
    if "colorTheme" in update_data:
        update_data["color_theme"] = update_data.pop("colorTheme").value.lower()

    for field, value in update_data.items():
        setattr(existing_pot, field, value)

    db.session.commit()
    return


def delete_pot(delete_pot_dto: DeletePotDto):
    existing_pot = get_pot_with_id_or_raise(delete_pot_dto.id)

    existing_pot.is_deleted = True

    db.session.commit()
    return
