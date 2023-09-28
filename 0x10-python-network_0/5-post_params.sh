#!/bin/bash
# Send a POST request to a URL and display the response body

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

# URL encode the data
data="email=$(urlencode "$email")&subject=$(urlencode "$subject")"

# Send the POST request with the encoded data and display the response body
curl -s "$url" -X POST -d "$data"

# Function to URL encode data
urlencode() {
  local data
  data=$(curl -Gso /dev/null -w %{url_effective} --data-urlencode "$1" "" 2>/dev/null)
  echo "${data##/?}"
}
