import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.services.prompt_builder import (
    build_review_prompt,
    build_diff_review_prompt,
)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_openai(prompt: str) -> dict:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.2,
    )

    content = response.output[0].content[0].text

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "bugs": [],
            "security": [],
            "improvements": [
                {
                    "title": "Invalid AI response format",
                    "severity": "medium",
                    "line": None,
                    "explanation": "The AI response could not be parsed as valid JSON.",
                    "suggestion": "Retry the request or adjust the prompt."
                }
            ]
        }


def review_code_with_ai(
    code: str,
    language: str | None = None,
    context: str | None = None,
) -> dict:
    prompt = build_review_prompt(code=code, language=language, context=context)
    return call_openai(prompt)


def review_diff_with_ai(diff: str) -> dict:
    prompt = build_diff_review_prompt(diff=diff)
    return call_openai(prompt)