from datetime import datetime, timedelta
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime


class Base(DeclarativeBase):
    pass


class URL(Base):

    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)

    short_code = Column(
        String(7),
        unique=True,
        index=True,
        nullable=False
    )

    original_url = Column(
        String(2048),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    expires_at = Column(
        DateTime,
        default=lambda: datetime.utcnow() + timedelta(hours=24),
        nullable=False
    )