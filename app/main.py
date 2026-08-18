from fastapi import FastAPI
from app.routers.url_router import router
from app.models import Base
from app.database import engine

app=FastAPI()

Base.metadata.create_all(bind=engine)
#if there is a failure in connecting to the postgres database then the SQLAlchemy is gnna raise a connection error 

app.include_router(router)
