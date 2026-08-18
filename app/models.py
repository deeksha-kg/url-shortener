from datetime import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column

class Base(DeclarativeBase):
    pass 

class URL(Base):
    __tablename__="urls"
    short_code: Mapped[str] = mapped_column(
        String(7),
        primary_key=True
    )
    original_url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    