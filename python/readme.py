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
        repo_name = event['repo']['name']
        if repo_name not in repos:
            repos[repo_name] = {
                'api':api_github(event['repo']['url']),
                'events': []
            }
        repo = repos[repo_name]
        if event['type'] == 'CreateEvent':
            repo['events'].append("Create Event")
            if event['payload']['ref_type'] == 'branch':
                ...
            elif event['payload']['ref_type'] == 'tag':
                ...
        elif event['type'] == 'DeleteEvent':
            repo['events'].append("Delete Event")
            if event['payload']['ref_type'] == 'branch':
                ...
            elif event['payload']['ref_type'] == 'tag':
                ...
        elif event['type'] == 'ForkEvent':
            forkLink = html_link(event['payload']['forkee']['full_name'],event['payload']['forkee']['html_url'])
            repo['events'].append(f"Created Fork {forkLink}")
        elif event['type'] == 'GollumEvent':
            repo['events'].append("Gollum Event")
        elif event['type'] == 'IssueCommentEvent':
            repo['events'].append("Issue Comment Event")
        elif event['type'] == 'IssuesEvent':
            issue = event['payload']['issue']
            issueLink = html_link(f"#{issue['number']}",issue['html_url'])
            if event['payload']['action'] in ['opened', 'closed', 'reopened']:
                verb = event['payload']['action'].capitalize()
                repo['events'].append(f"Issue <code>{issueLink}</code> {verb} - {issue['title']}")
            elif event['payload']['action'] == 'edited':
                repo['events'].append('Issue Edited')
            elif event['payload']['action'] == 'assigned':
                repo['events'].append('Issue Assigned')
            elif event['payload']['action'] == 'unassigned':
                repo['events'].append('Issue Unassigned')
            elif event['payload']['action'] == 'labeled':
                repo['events'].append('Issue Labeled')
            elif event['payload']['action'] == 'unlabeled':
                repo['events'].append('Issue Unlabeled')
        elif event['type'] == 'MemeberEvent':
            repo['events'].append("Member Event")
        elif event['type'] == 'PublicEvent':
            repo['events'].append("Repository is now Public")
        elif event['type'] == 'PullRequestEvent':
            repo['events'].append("Pull Request Event")
        elif event['type'] == 'PullRequestReviewEvent':
            repo['events'].append("Pull Request Review Event")
        elif event['type'] == 'PullRequestReviewCommentEvent':
            repo['events'].append("Pull Request Review Comment Event")
        elif event['type'] == 'PushEvent':
            branch = event['payload']['ref'].split('/')[2]
            for commit in event['payload']['commits']:
                sha = commit['sha'][:7].upper()
                commitApi = api_github(commit['url'])
                commitLink = html_link(f"#{sha}",commitApi['html_url'])
                message = commit['message'].partition('\n')[0]
                repo['events'].append(f"Commit <code>{commitLink} {branch}</code> {message}")
        elif event['type'] == 'ReleaseEvent':
            repo['events'].append("Release Event")
        elif event['type'] == 'SponsorshipEvent':
            repo['events'].append("Sponsorship Event")
        elif event['type'] == 'WatchEvent':
            repo['events'].append("Watch Event")
    reposOut = []
    for repo_name in repos:
        repo = repos[repo_name]
        repoLink = html_link(repo['api']['full_name'],repo['api']['html_url'])
        description = repo['api']['description']
        reposOut.append(html_details(f"{repoLink} - {description}",html_list(repo['events'])))
    return "".join(reposOut)



def section_community(user):
    print(html_header("Community",3))
    print(print_github_users("Followers",api_github(user['followers_url'])))
    print(print_github_users("Following",api_github(user['following_url'])))

def section_activity(user):
    events = api_github(user['events_url'].partition("{")[0] + "/public")
    print(html_header("Recent Activity",3))
    print(print_recent_repositories(events))

# Where the magic happens. This will output the markdown contents
if __name__ == "__main__":
    user = api_github("https://api.github.com/users/LittleTealeaf")
    print(print_json_file("LittleTealeaf.json",open_json("./assets/user.json")))
    section_community(user)
    section_activity(user)
