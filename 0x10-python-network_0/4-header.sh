#!/bin/bash
# This script is taking in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
