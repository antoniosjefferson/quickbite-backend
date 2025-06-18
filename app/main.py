from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app import user # import route file

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    create_db_and_tables()
    yield
    # Shutdown code (if any) can go here

app = FastAPI(lifespan=lifespan)
app.include_router(user.router) # register routes

@app.get("/")
def read_root():
    return {"message": "QuickBite API is live"}