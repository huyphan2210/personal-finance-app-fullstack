from typing import Optional
from uuid import UUID
from enums.color_enum import Color
from models.base_model import BaseModel


class Pot(BaseModel):
    id: str
    name: str
    target: float
    total: float
    colorTheme: Color


class Pots(BaseModel):
    pots: list[Pot]


class PotOverview(BaseModel):
    pots: list[Pot]
    totalSaved: float


class CreatePotDto(BaseModel):
    name: str
    target: float
    total: Optional[float] = None
    colorTheme: Color


class UpdatePotDto(BaseModel):
    id: UUID
    name: Optional[str] = None
    target: Optional[float] = None
    total: Optional[float] = None
    colorTheme: Optional[Color] = None


class DeletePotDto(BaseModel):
    id: UUID
