#!/bin/env sh
FILE="./github_token"
if test -f "$FILE"; then
    python3 ./python/readme.py $(cat $(ls | grep "github_token")) > README.md
else
    python3 ./python/readme.py "$METRICS_TOKEN" > README.md
fi
