#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./custom_github_script.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    if len(sys.argv) != 3:
        print("Usage: ./custom_github_script.py <GitHub username> <GitHub password>")
        sys.exit(1)

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)

    if r.status_code == 200:
        print(r.json().get("id"))
    else:
        print("Failed to retrieve GitHub ID. Status code:", r.status_code)


if __name__ == "__main__":
    main()
