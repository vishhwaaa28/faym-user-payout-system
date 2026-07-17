from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="User Payout Management System",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Faym User Payout Management System"
    }