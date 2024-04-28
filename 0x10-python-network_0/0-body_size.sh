#!/bin/bash
# This script sends a request to a URL and displays size of body of response
curl -sL "$1" | wc -c
