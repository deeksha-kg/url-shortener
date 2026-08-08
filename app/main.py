from fastapi import FastAPI
from app.routers.url_router import router

app=FastAPI()

app.include_router(router)
