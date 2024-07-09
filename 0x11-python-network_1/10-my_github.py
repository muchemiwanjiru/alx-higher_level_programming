#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    basic_auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # send a GET req to the github api for user info
    r = requests.get("https://api.github.com/user", auth=basic_auth)

    print(r.json().get("id"))
