from datetime import datetime
from database import db
from schemas.base_schema import BaseSchema


class Transaction(db.Model, BaseSchema):
    __tablename__ = "transactions"

    avatar_url = db.Column(db.String, nullable=True)
    user = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    amount = db.Column(db.Float, nullable=False)
    recurring = db.Column(db.Boolean, default=False)
