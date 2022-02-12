import json
import requests
from html import *
from icons import *

# Output is made using the "print()" method, as the output is piped into a file using the > operator

f_content = open("./resources/content.json")
content = json.load(f_content)
f_content.close()

f_events = open("./tmp/events.json")
events = json.load(f_events)
f_events.close()

def recent_repositories():
    print(header("Recent Activity",2))
    output = []
    repos = {}
    for event in events:
        repo = event['repo']
        if repo['name'] not in repos:
            repos[repo['name']] = {
                "url":repo['url'],
                "events": []
                }
        repos[repo['name']]['events'].append(event)

    for repo_name in repos:
        repo = repos[repo_name]
        revents = []
        for event in repo['events']:
            if event['type'] == 'PushEvent':
                for commit in event['payload']['commits']:
                    commit_link = link(f"#{commit['sha'][:7]}",f"https://www.github.com/{repo_name}/commit/{commit['sha']}")
                    message = commit['message'].partition('\n')[0]
                    revents.append(f"{commit_link} {message}")

        output.append(details(link(repo_name,f"https://www.github.com/{repo_name}"),hlist(revents)))

    return '\n'.join(output)

def badges_socials():
    return " ".join([create_icon(icons['socials'][name]) for name in icons['socials']])


def print_readme():
    print(header(content['title']))
    print(badges_socials())
    print(paragraph())
    print(paragraph())
    print(content['introduction'])

print(recent_repositories())
