from fastapi import FastAPI

from app.database import Base, engine
from app.users.routers import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["root"])
def root():
    return {"data": "welcome home!"}


app.include_router(user_router)
