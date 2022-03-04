import json
import requests
import sys

from assets import *
from formatting import *

github_token = ""

if len(sys.argv) > 1:
    github_token = sys.argv[1].partition('\r')[0]


username = "LittleTealeaf"

print(username)

