import uuid
from datetime import datetime
from sqlalchemy import UUID
from database import db
from models.category_model import Category


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    avatar_url = db.Column(db.String, nullable=True)
    user = db.Column(db.String, nullable=False)
    category = db.Column(db.Enum(Category), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    amount = db.Column(db.Float, nullable=False)
    recurring = db.Column(db.Boolean, default=False)
