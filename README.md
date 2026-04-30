# AI Code Review Engine

AI-powered backend that reviews code and returns:
- Bugs
- Security issues
- Improvements

## Tech Stack
- FastAPI
- OpenAI API
- Python

## Features
- Accepts raw code input
- Returns structured JSON feedback
- Detects runtime issues (e.g., division by zero)
- Suggests improvements

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload