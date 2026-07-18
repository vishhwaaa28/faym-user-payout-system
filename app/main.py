from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Faym User Payout System",
    description="User Payout Management System",
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Faym User Payout Management System"
    }