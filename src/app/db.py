import os

from databases import Database
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()


weather_requests = Table(
    "weather_requests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("country_code", String(50)),
    Column("city", String(50)),
    Column("date", String(50)),
    Column("response", String(500)),
    Column("created_date", DateTime, default=func.now(), nullable=False),

)

# databases query builder
database = Database(DATABASE_URL)
