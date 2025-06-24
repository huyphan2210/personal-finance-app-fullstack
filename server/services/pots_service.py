from schemas.pot_schema import Pot as PotSchema
from models.pots_model import Pot


def get_overview_pots():
    pots = PotSchema.query.filter_by(is_deleted=False).limit(4)

    return [
        Pot(
            name=pot.name,
            target=pot.target,
            total=pot.total,
            colorTheme=pot.color_theme,
        )
        for pot in pots
    ]
