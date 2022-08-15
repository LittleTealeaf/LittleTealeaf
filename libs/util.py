import json

def load_json(file):
    return open_file(file,json.load)

def open_file(file,action):
    with open(file) as f:
        return action(f)
