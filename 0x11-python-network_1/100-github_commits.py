#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of a repository by a user."""
import sys
import requests


def list_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(repo_name, owner_name)
