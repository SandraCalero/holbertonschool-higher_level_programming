#!/bin/bash
# This script is taking in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -c 8-
