import json
import requests

username = "LittleTealeaf"

def print_json(data):
    print_code(json.dumps(data),'json')

def print_code(code,language=''):
    print("```" + language)
    print(code)
    print("```")

def print_event(event):
    if event['type'] == 'PushEvent':
        print_json(event)
        commit_count = len(event['payload']['commits'])

        commits_plural = "commits"
        if commit_count == 1:
            commits_plural = "commit"
        
        repo = event['repo']['name']
        
        repo_json = requests.get(event['repo']['url']).json()

        # repo_link = repo_json["html_url"]
        repo_link = ""
        
        print(f" - Pushed {commit_count} {commits_plural} to [{repo}]({repo_link})")


def print_activity():
    events = requests.get(f"https://api.github.com/users/{username}/events").json()
    for i in range(5):
        print_event(events[i])


f = open("./resources/content.json")
data = json.load(f)
f.close()

print_activity()
followers = requests.get(f"https://api.github.com/users/{username}/followers").json()
