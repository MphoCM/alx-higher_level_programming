#!/bin/bash
#a Bsh script that takes in a URL as an argument and diplays the body of the response
curl -sH "X-School-User-Id: 98" "${1}"
