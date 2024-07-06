#!/bin/bash
# a URL that sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
