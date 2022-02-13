import json
import requests
from html import *

username = "LittleTealeaf"

# Output is made using the "print()" method, as the output is piped into a file using the > operator

def get_people(header,userList):
    string = ""
    for person in userList:
        string += link(image(person['avatar_url'],person['login'],"width:50px;height:50px"),person['html_url'])
    return details(header,string)



# f_content = open("./resources/content.json")
# content = json.load(f_content)
# f_content.close()
#
# f_events = open("./tmp/events.json")
# events = json.load(f_events)
# f_events.close()
# # events = requests.get(f"https://api.github.com/users/{username}/events").json()
#
# f_followers = open("./tmp/followers.json")
# followers = json.load(f_followers)
# f_followers.close()
#
# f_following = open("./tmp/following.json")
# following = json.load(f_following)
# f_following.close()

f_user = open("./assets/user.json")
userInfo = json.load(f_user)
f_user.close()

def json_block(jsonObject):
    jsonText = json.dumps(jsonObject,indent=2)
    return f"```json\n{jsonText}\n```"

if __name__ == "__main__":
    print(header("LittleTealeaf.json"))
    print()
    print(json_block(userInfo))
