#!/usr/bin/python3
# Task 0. What's my status? #0

import urllib.request

# Define the URL
url = 'https://alx-intranet.hbtn.io/status'

# Fetch the content from the URL
with urllib.request.urlopen(url) as response:
    # Read the response content
    content = response.read().decode("utf-8")

    # Display the content information
    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {content}')
