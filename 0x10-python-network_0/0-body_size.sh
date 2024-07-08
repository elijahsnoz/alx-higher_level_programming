#!/bin/bash
# Send a request to an URL with curl and display the size of the body of the response
echo "Sending request to: $1"
curl -s -w '%{size_download}' -o /dev/null "$1"
