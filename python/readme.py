import json
import requests
import sys
from resources import *

github_token = sys.argv[1].partition('\r')[0]

username = "LittleTealeaf"

load_gens()