from database import db
from sqlalchemy import func

from schemas.pot_schema import Pot as PotSchema
from models.pots_model import Pot, PotOverview


def get_overview_pots():
    pots = PotSchema.query.filter_by(is_deleted=False).limit(4).all()
    total_saved = (
        db.session.query(func.sum(PotSchema.total)).filter_by(is_deleted=False).scalar()
        or 0
    )

    return PotOverview(
        pots=[
            Pot(
                name=pot.name,
                target=pot.target,
                total=pot.total,
                colorTheme=pot.color_theme,
            )
            for pot in pots
        ],
        totalSaved=total_saved,
    )


def get_pots():
    pots = PotSchema.query.filter_by(is_deleted=False).all()
    return [
        Pot(
            name=pot.name,
            target=pot.target,
            total=pot.total,
            colorTheme=pot.color_theme,
        )
        for pot in pots
    ]
