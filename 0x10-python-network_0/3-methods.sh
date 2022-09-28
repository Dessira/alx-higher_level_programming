#!/bin/bash
# Bash Script displays allowed methods
curl -sI "$1" | grep "Allow: " | sed "s/Allow: //"
