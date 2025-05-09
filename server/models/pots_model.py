from models.base_model import BaseModel


class Pot(BaseModel):
    name: str
    target: float
    total: float


class Pots(BaseModel):
    pots: list[Pot]
