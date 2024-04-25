#!/bin/bash

# Check if both URL and filename arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Send a POST request with the contents of the file as JSON
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
