import json
import libs.github as github
from libs.markdown import *
from libs.util import *

def out(content: str):
    with open("README.md",'w') as file:
        file.write(content)

aboutme = code_block('json',json.dumps(load_json('config/aboutme.json'),indent=4))

out(f"""
{aboutme}
""")
