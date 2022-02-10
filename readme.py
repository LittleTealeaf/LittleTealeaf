import json
import requests

# see https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8

def details(name, content):
    return f"<details><summary>{name}</summary>{content}</details>"

def codeblock(code,language=""):
    return f"```{language}\n{code}\n```"

def link(content,link):
    return f"[{content}]({link})"

def quote(content):
    string = ""
    for line in content.split('\n'):
        string += f"> {line}  \n"
    return string

print(quote("I am a peanut\nhello\npie"))