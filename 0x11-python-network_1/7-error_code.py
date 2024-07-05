#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL,
displays the body of the response, and handles HTTP status errors.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
