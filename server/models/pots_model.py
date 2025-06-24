from enums.color_enum import Color
from models.base_model import BaseModel


class Pot(BaseModel):
    name: str
    target: float
    total: float
    colorTheme: Color


class Pots(BaseModel):
    pots: list[Pot]
