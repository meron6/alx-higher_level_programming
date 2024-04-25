#!/bin/bash

# Get the URL from the command line argument
url="$1"

# Send a DELETE request to the URL and display the body of the response
curl -sX DELETE "$url"
