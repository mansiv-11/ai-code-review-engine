from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.review import router as review_router

app = FastAPI(
    title="AI Code Review Engine",
    description="MVP backend for reviewing raw code or git diffs using AI.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_router, prefix="/api")


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Code Review Engine is running"
    }