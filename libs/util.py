import json

def load_json(file):
    with open(file) as f:
        return json.load(f)

def open_file(file,action):
    with open(file) as f:
        return action(f)
