import libs.cache as cache
import libs.github as github


content = ""
def write(c: str):
    global content
    content = content + c + "\n"








with open("./README.md",'w') as file:
    file.write(content)
