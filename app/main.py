from fastapi import FastAPI
from app.routes.review import router as review_router

app = FastAPI(
    title="AI Code Review Engine",
    description="MVP backend for reviewing raw code or git diffs using AI.",
    version="0.1.0",
)

app.include_router(review_router, prefix="/api")


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Code Review Engine is running"
    }