#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a POST request with the specified parameters
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
