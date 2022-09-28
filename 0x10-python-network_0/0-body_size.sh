#!/bin/bash
# Bash script that takes in a URL, sends a request and displays response size
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
