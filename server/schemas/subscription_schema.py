from datetime import datetime, timezone
from database import db
from schemas.base_schema import BaseSchema


class Subscription(db.Model, BaseSchema):
    __tablename__ = "subscriptions"

    avatar_url = db.Column(db.String, nullable=True)
    user = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    last_due = db.Column(
        db.DateTime, nullable=True, default=lambda: datetime.now(timezone.utc)
    )
    next_due = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    recurrence = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
