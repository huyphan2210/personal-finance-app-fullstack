import os
from flask import Flask
from database import db
from database.seed_data import seed_data


class DatabaseConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:1glpN0xybHxRTWFZzj8h@localhost:5432/financedb?sslmode=disable",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def connect_to_database(app: Flask):
    app.config.from_object(DatabaseConfig)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_data(db)
