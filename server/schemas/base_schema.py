import uuid
from datetime import datetime
from sqlalchemy import UUID
from sqlalchemy import DateTime, Boolean
from sqlalchemy.ext.declarative import declared_attr
from database import db


class BaseSchema:
    @declared_attr
    def id(cls):
        return db.Column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            unique=True,
            nullable=False,
        )

    @declared_attr
    def is_deleted(cls):
        return db.Column(Boolean, default=False)

    @declared_attr
    def created_at(cls):
        return db.Column(DateTime, default=datetime.now)

    @declared_attr
    def updated_at(cls):
        return db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
