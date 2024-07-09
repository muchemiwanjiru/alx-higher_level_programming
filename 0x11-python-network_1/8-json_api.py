#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    q = "" if len(sys.argv) == 1 else sys.argv[1]
    params = {"q": q}
    response = requests.post(url, data=params)
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print("Not a valid JSON")
