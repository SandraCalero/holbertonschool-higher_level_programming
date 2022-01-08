#!/bin/bash
# This script is taking in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2

# curl -s 0.0.0.0:5000 | wc -c is another option