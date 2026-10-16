from fastapi import FastAPI
from app.routers.url_router import router
from app.models import Base
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )

#if there is a failure in connecting to the postgres database then the SQLAlchemy is gnna raise a connection error 

app.include_router(router)
