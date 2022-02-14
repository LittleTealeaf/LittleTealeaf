import json
import requests
from html import *
from markdown import *

# Output is made using the "print()" method, as the output is piped into a file using the > operator

def open_json(fileName):
    file = open(fileName)
    jsonData = json.load(file)
    file.close()
    return jsonData

def print_github_users(header,userList):
    "I could make this one line, would that be effective? no... well..."
    string = ""
    for person in userList:
        image = html_image(person['avatar_url'],person['login'],"width:50px;height:50px")
        string += html_link(image,person['html_url'])
    return html_details(header,string)

def print_json_file(name,jsonObject):
    fileName = html_header(name,2)
    jsonBlock = json_block(jsonObject)
    return f"{fileName}\n\n{jsonBlock}"

if __name__ == "__main__":
    print(print_json_file("LittleTealeaf.json",open_json("./assets/user.json")))
