import json
import requests
import sys
from html import *
from markdown import *

github_token = sys.argv[1].partition('\r')[0]

username = "LittleTealeaf"

# Output is made using the "print()" method, as the output is piped into a file using the > operator

def open_json(fileName):
    file = open(fileName)
    jsonData = json.load(file)
    file.close()
    return jsonData

def api_github(url):
    return requests.get(url.partition("{")[0],headers={'authorization':f"token {github_token}"}).json()

def print_github_users(header,userList):
    "screw it, one line"
    imgAttr = "width:50px;height:50px"
    users = [html_link(html_img(person['avatar_url'],person['login'],imgAttr),person['html_url']) for person in userList]
    return html_details(header,"".join(users))

def print_json_file(name,jsonObject):
    fileName = html_header(name,2)
    jsonBlock = json_block(jsonObject)
    return f"{fileName}\n\n{jsonBlock}"

def print_recent_repositories(eventsJson):
    repos = []
    for event in eventsJson:
        if event['repo']['url'] not in repos:
            repos.append(event['repo']['url'])
    repoString = []
    for repo in repos[:5]:
        api = api_github(repo)
        link = html_link(api['full_name'],api['html_url'])
        repoString.append(f"{link} - {api['description']}")
    header = html_header("Recent Repositories",3)
    string = html_list(repoString)
    return f"{header}\n{string}"

def section_community(user):
    print(html_header("Community",3))
    print(print_github_users("Followers",api_github(user['followers_url'])))
    print(print_github_users("Following",api_github(user['following_url'])))


def section_activity(user):
    print(print_recent_repositories(api_github(user['events_url'])))

# Where the magic happens. This will output the markdown contents
if __name__ == "__main__":
    user = api_github("https://api.github.com/users/LittleTealeaf")
    print(print_json_file("LittleTealeaf.json",open_json("./assets/user.json")))
    section_community(user)
    section_activity(user)
