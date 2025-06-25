from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers import user, restaurant # import route file

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    create_db_and_tables()
    yield
    # Shutdown code (if any) can go here

app = FastAPI(lifespan=lifespan)
app.include_router(user.router) # register routes
app.include_router(restaurant.router)

@app.get("/")
def read_root():
    return {"message": "QuickBite API is live"}