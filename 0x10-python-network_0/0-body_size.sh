#!/bin/bash

# Get the URL from the command line argument
url="$1"

# Send a request to the URL and get the response body size in bytes
size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}')

# Display the size
echo "$size"
