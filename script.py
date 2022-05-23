import json
import libs.github as github
from libs.markdown import *
from libs.util import *

def out(content: str):
    with open("README.md",'w') as file:
        file.write(content)



user = github.getREST("https://api.github.com/users/LittleTealeaf")

print("Getting Stats")
stats_api = github.getGraphQL("""{
  user(login: "LittleTealeaf") {
    contributionsCollection {
      contributionYears
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            weekday
            date
          }
        }
      }
    }
  }
}""")

print("Getting Schemas")
schemas = github.getGraphQL("""{
  __schema {
    types {
      name
      kind
      description
      fields {
        name
      }
    }
  }
}""")

contributions = []

for week in stats_api['data']['user']['contributionsCollection']['contributionCalendar']['weeks']:
    for day in week['contributionDays']:
        contributions.append(day)

streak = 0
for c in contributions:
    if c['contributionCount'] > 0:
        streak += 1
    else:
        streak = 0


aboutme = code_block('json',json.dumps(load_json('config/aboutme.json'),indent=4))

stats = code_block('json',json.dumps({
    "total contributions": stats_api["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"],
    "consecutive days streak": streak
},indent=4))

out(f"{aboutme}\n{stats}\n*made with python*")
