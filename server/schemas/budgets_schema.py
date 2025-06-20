from database import db
from schemas.base_schema import BaseSchema


class Budget(db.Model, BaseSchema):
    __tablename__ = "budgets"

    category = db.Column(db.String, nullable=False)
    maximum = db.Column(db.Float, nullable=False)
    color_theme = db.Column(db.String, nullable=True)
    spent = db.Column(db.Float, nullable=True)
