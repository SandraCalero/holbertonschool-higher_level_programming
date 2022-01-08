#!/bin/bash
# This script is taking in a URL, sends a POST request to the passed URL, and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

# The -X option specifies which HTTP request method will be used when communicating with the remote server.
# The -d option Sends the specified data in a POST request to the HTTP server, in the same way that a browser
# does when a user has filled in an HTML form and presses the submit button