#!/bin/bash
# Send a GET request to a URL and display the body of the response if status code is 200
http_code=$(curl -sL -w "%{http_code}" -o /dev/null "$1")
echo "HTTP Status Code: $http_code"
if [ "$http_code" == '200' ]; then
    curl -sL "$1"
fi
