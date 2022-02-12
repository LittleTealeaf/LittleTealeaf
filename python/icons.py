import json

# https://github.com/alexandresanlim/Badges4-README.md-Profile

f_icons = open("./resources/icons.json")
icons = json.load(f_icons)
f_icons.close()

def icon_src(icon_json):
    attributes = '&'.join([f"{attribute}={icon_json['attributes'][attribute]}" for attribute in icon_json['attributes']])
    return f"https://img.shields.io/badge/{icon_json['name']}-{icon_json['color']}?{attributes}"

def create_icon(icon_json):
    src = icon_src(icon_json)
    return f"<a href=\"{icon_json['link']}\"><img src=\"{src}\"></a>"
