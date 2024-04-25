#!/bin/bash

# Get the URL from the command line argument
url="$1"

# Send an OPTIONS request to the URL and display the allowed methods
curl -sI "$url" | grep -i "Allow" | awk '{print $2}'
