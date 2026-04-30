def build_review_prompt(code: str, language: str | None = None, context: str | None = None) -> str:
    language_text = language or "unknown"
    context_text = context or "No additional context provided."

    return f"""
You are a strict senior software engineer doing a code review.

Return ONLY valid JSON.
Do not return markdown.
Do not return strings inside bugs, security, or improvements.
Every issue must be an object with these exact keys:
title, severity, line, explanation, suggestion.

Required JSON format:
{{
  "bugs": [],
  "security": [],
  "improvements": []
}}

STRICT CLASSIFICATION RULES:
- Division by zero risk MUST be classified as a bug.
- Null pointer risk MUST be classified as a bug.
- Runtime exceptions MUST be classified as bugs.
- Any logic that can crash execution MUST be classified as a bug.
- Security vulnerabilities go in security.
- Style/readability suggestions go in improvements.
- NEVER put crash risks or runtime exceptions in improvements.

Code:
{code}

Language:
{language_text}

Context:
{context_text}
"""


def build_diff_review_prompt(diff: str) -> str:
    return f"""
You are a strict senior software engineer reviewing a Git diff.

Analyze only the added lines in the diff.

Return ONLY valid JSON.
Do not return markdown.
Do not return strings inside bugs, security, or improvements.
Every issue must be an object with these exact keys:
title, severity, line, explanation, suggestion.

Required JSON format:
{{
  "bugs": [],
  "security": [],
  "improvements": []
}}

STRICT CLASSIFICATION RULES:
- Division by zero risk MUST be classified as a bug.
- Null pointer risk MUST be classified as a bug.
- Runtime exceptions MUST be classified as bugs.
- Any logic that can crash execution MUST be classified as a bug.
- Security vulnerabilities go in security.
- Style/readability suggestions go in improvements.
- NEVER put crash risks or runtime exceptions in improvements.

Git diff:
{diff}
"""