import json
import requests
import sys

from assets import *
from formatting import *

github_token = ""

if len(sys.argv) > 1:
    github_token = sys.argv[1].partition('\r')[0]

username = "LittleTealeaf"

initialize_assets()

def api_github(url):
    return requests.get(url.partition("{")[0],headers={'authorization':f"token {github_token}"}).json()

def print_socials():
    images = load_json(get_asset_path('socials.json'))
    return " ".join([ html_link(html_img(image['img']),image['link']) for image in images])

def print_userjson():
    return markdown_pretty_json(load_json(get_asset_path('user.json')))




print(print_userjson())
print(print_socials())
