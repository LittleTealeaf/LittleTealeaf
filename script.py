import json
import os
from libs.cache import clean_cache
import libs.github as github
from libs.markdown import *
from libs.util import *
import libs.wakatime as wakatime

clean_cache()


def out(content: str):
    with open("README.md", "w") as file:
        file.write(content)


about_me = code_block("json", json.dumps(load_json("config/aboutme.json"), indent=2))


# waka_all = wakatime.getData("/api/v1/users/current/stats/all_time")["data"]
# waka_monthly = wakatime.getData("/api/v1/users/current/stats/last_30_days")["data"]
# waka_weekly = wakatime.getData("/api/v1/users/current/stats/last_7_days")["data"]
waka_all = wakatime.getStats("all_time")
waka_monthly = wakatime.getStats("last_30_days")
waka_weekly = wakatime.getStats("last_7_days")

current_projects = waka_weekly["projects"][0:10]


def format_current_project(project):
    name = project["name"]
    description = ""
    waka_project = wakatime.getData(
        f'/api/v1/users/LittleTealeaf/projects/{project["name"]}'
    )["data"]
    if waka_project["repository"] != None:
        github_api = github.getREST(waka_project["repository"]["url"])
        name = f"<a href=\"{github_api['html_url']}\">{github_api['full_name']}</a> ({github_api['language']})"
        description = '<br>' + github_api['description']

    return f"{name} - {project['text']}{description}"

current_projects = [format_current_project(project) for project in current_projects]

def format_waka_list(data):
    return ", ".join(item['name'] for item in data)




out(
    f"""
### Hello There! I'm Thomas Kwashnak

- Undergraduate Student at Quinnipiac University studying Computer Science and Data Science, with a minor in economics.
- Not currently looking for a job, but wide open for internship opportunities for Summer 2023
- I'm an "anything-but-apple" enthusiast. Doesn't mean I completely dispise apple, just means I personally prefer other companies.

### What I'm Working On (Last 7 days)
{bullet_list(current_projects)}

### Recently Used Tools and Languages (Last 30 days)
- **Operating Systems**: {format_waka_list(waka_monthly['operating_systems'][0:5])}
- **Code Editors**: {format_waka_list(waka_monthly['editors'][0:5])}
- **Languages**: {format_waka_list(waka_monthly['languages'][0:10])}

### Most Used Tools and Languages
- **Operating Systems**: {format_waka_list(waka_all['operating_systems'][0:5])}
- **Code Editors**: {format_waka_list(waka_all['editors'][0:5])}
- **Languages**: {format_waka_list(waka_all['languages'][0:10])}

*auto-generated using python*
"""
)
