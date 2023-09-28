#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL."
    exit 1
fi

http_status_code=$(curl -si "$1" -X GET | head -n 1 | awk '{print $2}')

if [ "$http_status_code" = '200' ]; then
    curl -sL "$1"
else
    echo "HTTP Status Code: $http_status_code"
fi
