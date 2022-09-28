#!/bin/bash
# Bash script that sends a JSON POST request to a URL
curl -s -o /dev/null -w "%{http_code}" "$1"
