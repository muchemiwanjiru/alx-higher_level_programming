#!/usr/bin/python3
"""
script that takes and prints the 10 latest commits from a github repo
usage: ./100-github_commits.py <repository name> <user/owner name>
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    response = requests.get(url.format(argv[2], argv[1]))
    resp =response.json()
    try:
        for i in range(0, 10):
            print(f"{resp[i].get('sha')}: \
{resp[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
