#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL."
    exit 1
fi

response=$(curl -sX DELETE "$1")

echo "Response Body:"
echo "$response"
