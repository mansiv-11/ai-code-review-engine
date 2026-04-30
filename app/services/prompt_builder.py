def build_review_prompt(code: str, language: str | None = None, context: str | None = None) -> str:
    language_text = language or "unknown"
    context_text = context or "No additional context provided."

    return f"""
You are a senior software engineer doing a strict code review.

Return ONLY valid JSON.
Do not return markdown.
Do not return strings inside bugs, security, or improvements.
Every issue must be an object with these exact keys:
title, severity, line, explanation, suggestion.

Required JSON format:
{{
  "bugs": [
    {{
      "title": "Short bug title",
      "severity": "low | medium | high",
      "line": 1,
      "explanation": "Why this is a bug",
      "suggestion": "How to fix it"
    }}
  ],
  "security": [],
  "improvements": [
    {{
      "title": "Short improvement title",
      "severity": "low | medium | high",
      "line": 1,
      "explanation": "Why this improves the code",
      "suggestion": "Specific improvement"
    }}
  ]
}}

Classification rules:
- Runtime failure risks go in bugs
- Security vulnerabilities go in security
- Style, readability, maintainability, and performance suggestions go in improvements
- If a category has no issues, return []

Code:
{code}

Language:
{language_text}

Context:
{context_text}
"""