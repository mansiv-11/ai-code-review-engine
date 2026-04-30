def build_review_prompt(code: str, language: str | None = None, context: str | None = None) -> str:
    return f"""
Analyze the following {language} code.

Code:
{code}

Context:
{context}

Return STRICT JSON in this format:
{{
  "bugs": [{{"title": "", "severity": "", "line": 0, "explanation": "", "suggestion": ""}}],
  "security": [{{"title": "", "severity": "", "line": 0, "explanation": "", "suggestion": ""}}],
  "improvements": [{{"title": "", "severity": "", "line": 0, "explanation": "", "suggestion": ""}}]
}}

Rules:
- Always return at least 2 improvements
- Be specific and actionable
- Include best practices, readability, and performance
- If no security issues, return empty list
"""