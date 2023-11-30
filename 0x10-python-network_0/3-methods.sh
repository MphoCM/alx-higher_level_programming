#!/bin/bash
#scrpt takes URL nad displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
