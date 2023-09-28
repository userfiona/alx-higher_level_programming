#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL using curl and save the response in a temporary file
response_file=$(mktemp)
curl -s "$1" > "$response_file"

# Check if the request was successful
if [ $? -ne 0 ]; then
  echo "Failed to retrieve the URL."
  rm -f "$response_file"
  exit 1
fi

# Get the size of the response body in bytes
body_size=$(wc -c < "$response_file")

# Display the size of the body in bytes
echo "Size of the body of the response: $body_size bytes"

# Clean up the temporary file
rm -f "$response_file"
