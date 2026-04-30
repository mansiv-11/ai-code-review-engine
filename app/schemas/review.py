from typing import List, Optional
from pydantic import BaseModel, Field


class ReviewRequest(BaseModel):
    code: str = Field(..., description="Raw code or git diff to review")
    language: Optional[str] = Field(default=None, description="Programming language")
    context: Optional[str] = Field(default=None, description="Optional project context")


class ReviewIssue(BaseModel):
    title: str
    severity: str
    line: Optional[int] = None
    explanation: str
    suggestion: str


class ReviewResponse(BaseModel):
    bugs: List[ReviewIssue]
    security: List[ReviewIssue]
    improvements: List[ReviewIssue]