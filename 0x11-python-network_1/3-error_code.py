#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
