#!/bin/bash

# Get the URL from the command line argument
url="$1"

# Send a GET request to the URL and display the body of the response
curl -sL -w "%{http_code}" "$url" | grep -q "200" && curl -sL "$url"
