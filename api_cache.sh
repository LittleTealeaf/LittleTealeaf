#!/bin/env sh
mkdir tmp
cd tmp
wget https://api.github.com/users/LittleTealeaf/followers -O followers.json
wget https://api.github.com/users/LittleTealeaf/events -O events.json