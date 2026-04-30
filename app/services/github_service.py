import re
import requests


def fetch_pr_diff(pr_url: str) -> str:
    if not pr_url:
        raise ValueError("PR URL is required")

    match = re.match(
        r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)",
        pr_url.strip()
    )

    if not match:
        raise ValueError("Invalid GitHub PR URL. Expected format: https://github.com/owner/repo/pull/123")

    owner, repo, pr_number = match.groups()
    diff_url = f"https://github.com/{owner}/{repo}/pull/{pr_number}.diff"

    response = requests.get(diff_url, timeout=15)

    if response.status_code != 200:
        raise ValueError("Unable to fetch PR diff. Make sure the PR is public and the URL is correct.")

    return response.text