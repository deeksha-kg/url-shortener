from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL)
# the engine is like a database connection manager which knows WHERE the db is , 
# knows HOW to connect , 
# manages connections and 
#maintains a connection pool

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)