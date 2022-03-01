import json
import requests
import sys
from html_formatting import *
from markdown_formatting import *
from image_formatting import *

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
    imgAttr = "width:30px;height:30px"

    users = []
    for person in userList:
        imgsrc = image_format_src(person['avatar_url'],make_circular=True)
        img = html_img(imgsrc,person['login'],imgAttr)
        link = html_link(img,person['html_url'])
        users.append(link)
    
    return html_tag("b",header) + ":<br>" + "".join(users) + "<br>"

def print_json_file(name,jsonObject):
    fileName = html_header(name,2)
    jsonBlock = json_block(jsonObject)
    return f"{fileName}\n\n{jsonBlock}"

def print_recent_repositories(events):
    max_text_length = 50

    def format_message(message):
        msg = message.partition('\n')[0].split(' ')
        count = 0
        string = []
        while count < max_text_length and len(msg) > 0:
            s = msg.pop(0)
            count += len(s)
            string.append(s)
        if len(msg) > 0:
            return ' '.join(string) + "..."
        else:
            return ' '.join(string)

    def format_event(event):
        t = event['type']
        payload = event['payload']
        if t == 'CommitCommentEvent':

            message = format_message(payload['comment']['body'].partition('\n')[0])
            commitLink = html_link(f"#{payload['comment']['commit_id'][:7]}",payload['comment']['html_url'])

            return f"Commented on commit {commitLink}: \"{message}\""

        elif t in ['CreateEvent', 'DeleteEvent']:

            verb = event['type'].replace('Event','d')
            createType = payload['ref_type'].capitalize()
            return f"{verb} {createType}: {payload['ref']}"
        
        elif t == 'ForkEvent':

            forkLink = html_link(payload['forkee']['name'],payload['forkee']['html_url'])
            return f"Created Fork {forkLink}"

        elif t == 'GollumEvent':

            pages = ", ".join([html_link(page['page_name'],page['html_url']) for page in payload['pages']])
            return f"Updated Wiki Pages: {pages}"

        elif t == 'IssueCommentEvent':
            issueLink = html_link(f"#{payload['issue']['number']} {payload['issue']['title']}",payload['comment']['html_url'])

            if payload['action'] == 'created':
                return f"Commented on issue {issueLink}"

            elif payload['action'] == 'edited':
                return f"Edited comment on issue {issueLink}"
            
            elif payload['action'] == 'deleted':
                issueLink = html_link(f"#{payload['issue']['number']}",payload['issue']['html_url'])
                return f"Deleted comment on issue {issueLink}"

        elif t == 'IssuesEvent':
            a = payload['action']
            issueLink = html_link(f"#{payload['issue']['id']}",payload['issue']['html_url'])

            if a in ['opened', 'edited', 'closed', 'reopened']:
                verb = a.capitalize()
                return f"{verb} issue {issueLink}"

            elif a in ['labeled', 'unlabeled']:
                verb = 'Added'
                if a == 'unlabeled':
                    verb = 'Removed'
                return f"{verb} Label <code>{payload['label']}</code> to issue {issueLink}"
            elif a in ['assigned','unassigned']:

                verb = 'Added'
                if a == 'unassigned':
                    verb = 'Removed'
                assigneeLink = html_link(payload['assignee']['login'],payload['assignee']['html_url'])
                return f"{verb} {assigneeLink} to issue {issueLink}"
        
        elif t == 'MemberEvent':
            return None # TODO: Figure this out?

        elif t == 'PublicEvent':
            return "Repository is now public!"
        
        elif t == 'PullRequestEvent':
            a = payload['action']
            prLink = html_link(f"#{payload['pull_request']['number']} {payload['pull_request']['title']}",payload['pull_request']['html_url'])

            if a in ['opened', 'edited', 'closed', 'reopened', 'synchronized']:
                verb = a.capitalize()
                return f"{verb} Pull Request {prLink}"
        
        elif t == 'PullRequestReviewEvent':
            a = payload['review']['event']
            prLink = html_link(f"#{payload['pull_request']['number']} {payload['pull_request']['title']}",payload['pull_request']['html_url'])

            if a == 'APPROVE':
                return f"Reviewed Pull Request {prLink}: Approved"
            elif a == 'REQUEST_CHANGES':
                return f"Reviewed Pull Request {prLink}: Requesting Changes"
            elif a == 'COMMENT':
                return f"Reviewed Pull Request {prLink}: Added Comment"
            # elif a == 'PENDING':
            #     return f"Reviewed Pull Request {prLink}: Pending"
        
        elif t == 'PullRequestReviewCommentEvent':
            return None # TODO figure out what this is
        
        elif t == 'PushEvent':
            repoApi = api_github(event['repo']['url'])
            repoLink = html_link(repoApi['name'],repoApi['html_url'])

            branch = payload['ref'].split('/')[-1]

            if payload['size'] > 1:
                commits = []
                for commit in payload['commits']:
                    commitApi = api_github(commit['url'])
                    commitLink = html_link(f"#{commitApi['sha'][:7]}",commitApi['html_url'])
                    message = format_message(commitApi['commit']['message'])
                    commits.append(f"{commitLink}: {message}")
    
               
                
                commitList = html_list(commits)

                commitCount = len(commits)
                return f"Pushed {commitCount} commits to <code>{branch}</code>{commitList}"
            
            else:
                commit = payload['commits'][0]
                commitApi = api_github(commit['url'])
                commitLink = html_link(f"#{commitApi['sha'][:7]}",commitApi['html_url'])
                message = format_message(commitApi['commit']['message'])

                return f"Pushed to <code>{branch}</code> {commitLink}: {message}"
        
        elif t == 'ReleaseEvent':
            a = payload['action']
            releaseLink = html_link(payload['release']['name'],payload['release']['html_url'])

            if a == 'published':    
                return f"Released {releaseLink}"
            elif a == 'edited':
                return f"Modified {releaseLink}"

        return None
        

    printEvents = {}
    for event in events:
        if event['repo']['name'] not in printEvents:
            formattedEvent = format_event(event)
            if formattedEvent:
                repoApi = api_github(event['repo']['url'])
                repoLink = html_link(event['repo']['name'],repoApi['html_url'])
                repoDescription = repoApi['description']
                if repoDescription == 'None':
                    repoDescription = 'No Description'
                printEvents[event['repo']['name']] = f"{repoLink} - {repoDescription}<br>{formattedEvent}"

    repos = [printEvents[repo] for repo in printEvents]
    return html_list(repos)


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
