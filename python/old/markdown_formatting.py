import json

def json_block(jsonObject):
    jsonText = json.dumps(jsonObject,indent=2)
    return f"```json\n{jsonText}\n```"
