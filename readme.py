import json
import requests

def get(url):
    return requests.get(url).json()

def get_data():
    f = open("./resources/content.json")
    data = json.load(f)
    f.close()
    return data

def about_me(data):
    print("### About Me")
    print(data["about_me"])


data = get_data()
followers = get("https://api.github.com/users/LittleTealeaf/followers")
repositories = get("https://api.github.com/users/LittleTealeaf/repos")
#   https://api.github.com/repos/octocat/hello-world/commits



print(data["intro"])
about_me(data)