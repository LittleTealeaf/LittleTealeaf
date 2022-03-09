#!/bin/env sh
FILE="./github_token"
python3 -m pip install -r ./python/requirements.txt
if test -f "$FILE"; then
    python3 ./python/readme.py $(cat $(ls | grep "github_token")) > README.md
else
    python3 ./python/readme.py "$GITHUB_TOKEN" > README.md
fi
