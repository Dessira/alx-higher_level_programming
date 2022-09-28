#!/bin/bash
# script must send a POST request with the contents of a file
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
