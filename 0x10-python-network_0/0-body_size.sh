#!/bin/bash
# Get the size of the response body
curl -s "$1" | wc -c

