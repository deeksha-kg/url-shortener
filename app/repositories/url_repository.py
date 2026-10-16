from sqlalchemy import select
from app.database import SessionLocal
from app.models import URL

def save(short_code: str,original_url: str):
    db=SessionLocal()
    try:
        url=URL(
            short_code=short_code,
            original_url=original_url
        )
        db.add(url)
        db.commit()
    finally:
        db.close()
 

def get(short_code: str):
    db=SessionLocal()
    try:
        statement=select(URL).where(URL.short_code==short_code)
        result=db.execute(statement)
        return result.scalar_one_or_none()
    finally:
        db.close()


def exists(short_code: str):
    db=SessionLocal()
    try:
        statement=select(URL).where(URL.short_code==short_code)
        result=db.execute(statement)
        return result.scalar_one_or_none() is not None
    finally:
        db.close()

def get_by_original_url(original_url: str):

    db = SessionLocal()

    try:
        statement = select(URL).where(
            URL.original_url == original_url
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    finally:
        db.close()
