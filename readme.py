import json
import requests

# see https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8

def print_json(json_data):
    return md_codeblock(json.dumps(json_data),'json')

def html_details(name, content):
    return f"<details><summary>{name}</summary>{content}</details>"

def html_image(source,alt,style=""):
    return f"<img src=\"{source}\" alt=\"{alt}\" style=\"{style}\">"

def html_link(link,content):
    return f"<a href=\"{link}\">{content}</a>"
        

def md_codeblock(code,language=""):
    return f"```{language}\n{code}\n```"

def md_link(content,link):
    return f"[{content}]({link})"

def md_quote(content):
    string = ""
    for line in content.split('\n'):
        string += f"> {line}  \n"
    return string

def html_list(content,tag="ul"):
    string = f"<{tag}>"
    for item in content:
        string += f"<li>{item}</li>"
    string += f"</{tag}>"
    return string


def fetch_events():
    f = open("./tmp/events.json")
    data = json.load(f)
    f.close()
    return data

def fetch_followers():
    f = open("./tmp/followers.json")
    data = json.load(f)
    f.close()
    return data

def fetch_following():
    f = open("./tmp/following.json")
    data = json.load(f)
    f.close()
    return data

def fetch_user():
    f = open("./tmp/user.json")
    data = json.load(f)
    f.close()
    return data

def build_following():
    string = ""
    for user in fetch_following():
        string += html_link(user['html_url'],html_image(user['avatar_url'],user['login'],"width:42px;height:42px"))
    return html_details("Following",string)

def build_followers():
    string = ""
    for user in fetch_followers():
        string += html_link(user['html_url'],html_image(user['avatar_url'],user['login'],"width:42px;height:42px"))
    return html_details("Followers",string)


def build_events():
    string = ""
    events_json = fetch_events()
    for i in range(10):
        event = events_json[i]
        commits_count = len(event['payload']['commits'])
        event_link = html_link(f"https://github.com/{event['repo']['name']}",event['repo']['name'])
        event_title = f"Pushed {commits_count} commits to {event_link}"
        string += html_details(event_title,"")    
    return html_details("Recent Activity",string)

def build_event_push():
    string = ""

    return string

print(build_followers())
print(build_following())
print(build_events())