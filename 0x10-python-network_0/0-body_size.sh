#!/bin/bash
# This script sends a request to a URL and displays the size of the
# body of the response

url=$1
response_body=$(curl -s "$url")
response_size=$(echo -n "$response_body" | wc -c)
echo "$response_size"
