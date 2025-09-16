
from datetime import datetime, timezone
from sqlalchemy import UUID
from database import db
from schemas.base_schema import BaseSchema
from database import LOCAL_DB_NAME

class Transaction(db.Model, BaseSchema):
    __tablename__ = f"{LOCAL_DB_NAME}_transactions"

    avatar_url = db.Column(db.String, nullable=True)
    user = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    amount = db.Column(db.Float, nullable=False)
    subscription_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey(f"{LOCAL_DB_NAME}_subscriptions.id"),
        nullable=True,
    )
