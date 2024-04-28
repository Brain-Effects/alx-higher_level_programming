#!/bin/bash
# This script sends a request to a URL and displays the size of the body of the response

url=$1
response_size=$(curl -sL "$url" | wc -c)
echo "$response_size"
