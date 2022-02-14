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

def print_recent_repositories(events):
    repos = {}
    for event in events:
        if event['repo']['url'] not in repos:
            repos[event['repo']['url']] = [event]
        else:
            repos[event['repo']['url']].append(event)
    reposOut = []
    for repo in repos:
        repoApi = api_github(repo)
        repoLink = html_link(repoApi['full_name'],repoApi['html_url'])
        description = repoApi['description']
        events = []
        for event in repos[repo]:
            if event['type'] == 'CreateEvent':
                ...
            elif event['type'] == 'DeleteEvent':
                ...
            elif event['type'] == 'ForkEvent':
                forkLink = html_link(event['payload']['forkee']['full_name'],event['payload']['forkee']['html_url'])
                events.append(f"Created Fork {forkLink}")
            elif event['type'] == 'GollumEvent':
                ...
            elif event['type'] == 'IssueCommentEvent':
                ...
            elif event['type'] == 'IssueEvent':
                ...
            elif event['type'] == 'MemberEvent':
                ...
            elif event['type'] == 'PublicEvent':
                ...
            elif event['type'] == 'PullRequestEvent':
                ...
            elif event['type'] == 'PullRequestReviewEvent':
                ...
            elif event['type'] == 'PullRequestReviewCommentEvent':
                ...
            elif event['type'] == 'PushEvent':
                branch = event['payload']['ref'].split('/')[2]
                for commit in event['payload']['commits']:
                    sha = commit['sha'][:7]
                    commitApi = api_github(commit['url'])
                    commitLink = html_link(f"#{sha}",commitApi['html_url'])
                    message = commit['message'].partition('\n')[0]
                    events.append(f"<code>{branch}</code> {commitLink} - {message}")
            elif event['type'] == 'ReleaseEvent':
                ...
            elif event['type'] == 'SponsorshipEvent':
                ...
            elif event['type'] == 'WatchEvent':
                ...

            # TODO: add "Merge Request" and such
            # See https://docs.github.com/en/developers/webhooks-and-events/events/github-event-types
        reposOut.append(html_details(f"{repoLink} - {description}",html_list(events)))
    return "".join(reposOut)



def section_community(user):
    print(html_header("Community",3))
    print(print_github_users("Followers",api_github(user['followers_url'])))
    print(print_github_users("Following",api_github(user['following_url'])))

def section_activity(user):
    events = api_github(user['events_url'] + "/public")
    print(html_header("Recent Activity",3))
    print(print_recent_repositories(events))

# Where the magic happens. This will output the markdown contents
if __name__ == "__main__":
    user = api_github("https://api.github.com/users/LittleTealeaf")
    print(print_json_file("LittleTealeaf.json",open_json("./assets/user.json")))
    # section_community(user)
    section_activity(user)
