import json
import requests
import sys

from asset_manager import *
from print_formatting import *
from image_formatting import *


username = "LittleTealeaf"
github_token = ""

if len(sys.argv) > 1:
    github_token = sys.argv[1].partition('\r')[0]

def api_github(url):
    return requests.get(url.partition("{")[0],headers={'authorization':f"token {github_token}"}).json()


user = api_github(f"https://api.github.com/users/{username}")

initialize_assets()

def print_socials():
    images = load_json(get_asset_path('socials.json'))
    return " ".join([ html_link(html_img(image['img']),image['link']) for image in images])

def print_userjson():
    return markdown_pretty_json(load_json(get_asset_path('user.json')))

def print_users(users,size="30px"):
    images = []
    for u in users:
        img_src = generate_asset_path(u['login'] + str(size) + "circular","png")
        image_format(image_src(u['avatar_url']),attributes={'circular':True}).save(img_src)
        image = html_img(img_src,alt=u['login'],style=f"width:{size};height:{size}")
        images.append(html_link(image,u['html_url']))
    return " ".join(images)



print(print_userjson())
print(print_socials())

print("<br>")
print(print_users(api_github(user['following_url'])))
