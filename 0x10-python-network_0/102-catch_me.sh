#!/bin/bash

# Make a request to the specified URL with a custom User-Agent header
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" "$1"
