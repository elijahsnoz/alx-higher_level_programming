#!/usr/bin/python3
"""
A script that lists 10 commits (from the most recent to oldest)
of a repository by user.
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
