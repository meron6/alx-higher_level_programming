#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
