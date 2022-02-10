import json
import requests

# see https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8

def details(name, content):
    return f"<details><summary>{name}</summary>{content}</details>"

def codeblock(code,language=""):
    return f"""```{language}\n{code}\n```"""

print(details("Code",codeblock("sudo apt install java","bash")))