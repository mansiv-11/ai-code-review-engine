from fastapi import APIRouter, HTTPException

from app.schemas.review import ReviewRequest, ReviewResponse
from app.services.reviewer import review_code_with_ai

router = APIRouter()


@router.post("/review", response_model=ReviewResponse)
def review_code(request: ReviewRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code input cannot be empty")

    try:
        result = review_code_with_ai(
            code=request.code,
            language=request.language,
            context=request.context,
        )
        return result
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))