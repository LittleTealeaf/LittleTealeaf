#!/bin/env sh
python3 ./python/readme.py $(cat $(ls | grep "github_token")) > README.md
