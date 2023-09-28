#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

# URL encode the data
data="email=$(urlencode "$email")&subject=$(urlencode "$subject")"

# Send the POST request with the encoded data
curl -s "$url" -X POST -d "$data"

# Function to URL encode data
urlencode() {
  local data
  data=$(curl -Gso /dev/null -w %{url_effective} --data-urlencode "$1" "" 2>/dev/null)
  echo "${data##/?}"
}
