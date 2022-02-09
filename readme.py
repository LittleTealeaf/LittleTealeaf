import json

def get_data():
    f = open("./resources/content.json")
    data = json.load(f)
    f.close()
    return data

def about_me(data):
    print("### About Me")
    print(data["about_me"])


data = get_data()

print(data["intro"])
about_me(data)
