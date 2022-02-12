import json
import requests
from html import *

# Output is made using the "print()" method, as the output is piped into a file using the > operator

f_content = open("./resources/content.json")
content = json.load(f_content)
f_content.close()





print(header(content['title']))
print(content['introduction'])
