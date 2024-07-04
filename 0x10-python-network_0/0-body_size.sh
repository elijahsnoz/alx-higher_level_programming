#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

# Check if a URL was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to get the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

