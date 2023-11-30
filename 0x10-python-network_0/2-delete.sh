#!/bin/bash
# a Bash script that takes in URL and displays allmHTTP methods the server will accept.
curl -sX OPTIONS -I "$1" | grep -1 "Allow:" | cut -d ' ' -f 2-
