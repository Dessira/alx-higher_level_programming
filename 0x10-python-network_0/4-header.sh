#!/bin/bash
# Bash Script takes X-School-User-Id header variable
curl -sX GET -H "X-School-User-Id" "$1"
