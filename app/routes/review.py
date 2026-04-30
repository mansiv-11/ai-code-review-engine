from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.schemas.review import ReviewRequest, ReviewResponse
from app.services.github_service import fetch_pr_diff
from app.services.reviewer import review_code_with_ai, review_diff_with_ai

router = APIRouter()


class DiffRequest(BaseModel):
    diff: str


class PRRequest(BaseModel):
    pr_url: str


@router.post("/review", response_model=ReviewResponse)
def review_code(request: ReviewRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code input cannot be empty")

    try:
        return review_code_with_ai(
            code=request.code,
            language=request.language,
            context=request.context,
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/review-diff", response_model=ReviewResponse)
def review_diff(request: DiffRequest):
    if not request.diff.strip():
        raise HTTPException(status_code=400, detail="Diff input cannot be empty")

    try:
        return review_diff_with_ai(diff=request.diff)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/review-pr", response_model=ReviewResponse)
def review_pr(request: PRRequest):
    if not request.pr_url.strip():
        raise HTTPException(status_code=400, detail="PR URL cannot be empty")

    try:
        diff = fetch_pr_diff(request.pr_url)
        return review_diff_with_ai(diff=diff)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))