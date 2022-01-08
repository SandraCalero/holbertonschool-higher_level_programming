#!/bin/bash
# This script is taking in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
