from fastapi import FastAPI
from app.database import engine
from app.router import user
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router)

@app.get("/")
def get_user():
    return {"hi":"backend is working"}