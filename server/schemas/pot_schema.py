from database import db
from schemas.base_schema import BaseSchema
from database import LOCAL_DB_NAME

class Pot(db.Model, BaseSchema):
    __tablename__ = f"{LOCAL_DB_NAME}_pots"

    name = db.Column(db.String, nullable=False)
    target = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    color_theme = db.Column(db.String, nullable=True)
