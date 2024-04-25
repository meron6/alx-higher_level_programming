#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request with the specified header
curl -sH "X-School-User-Id: 98" "$1"
