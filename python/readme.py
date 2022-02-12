import json
import requests
from html import *
from icons import *

# Output is made using the "print()" method, as the output is piped into a file using the > operator

f_content = open("./resources/content.json")
content = json.load(f_content)
f_content.close()



def badges_socials():
    return " ".join([create_icon(icons['socials'][name]) for name in icons['socials']])



print(header(content['title']))
print(badges_socials())
print(paragraph())
print(paragraph())g
print(content['introduction'])
