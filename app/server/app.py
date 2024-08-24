from fastapi import FastAPI
from app.server.database import init_db
from app.server.routes.review_routes import router as Router


app = FastAPI()
app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    try:
        await init_db()
    except Exception as e:
        print(f"Error occurred during startup: {e}")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FastAPI with beanie app!"}

