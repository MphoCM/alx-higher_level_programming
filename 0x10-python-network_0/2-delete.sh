#!/bin/bash
# a Bash script that takes in URL and displays allmHTTP methods the server will accept.
curl -sX OPTIONS "$1"
