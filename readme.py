import json

def get_data():
    f = open("./resources/content.json")
    data = json.load(f)
    f.close()
    return data


data = get_data()
