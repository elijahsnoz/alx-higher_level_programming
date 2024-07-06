#!/usr/bin/python3
"""A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user ID.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = f"https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get("id")
        print(user_id)
    else:
        print(None)
