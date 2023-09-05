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

waka_all = wakatime.getStats("all_time")
waka_monthly = wakatime.getStats("last_30_days")
waka_weekly = wakatime.getStats("last_7_days")

assert waka_weekly is not None
assert waka_monthly is not None
assert waka_all is not None

current_projects = waka_weekly["projects"][0:10]

def format_waka_list(data,percentage=False,time=False):
    values = []
    for item in data:
        name = item['name']
        if percentage:
            values.append(f"{name} ({item['percent']}%)")
            continue
        if time:
            values.append(f"{name} ({item['text']})")
            continue
        values.append(name)

    return ", ".join(values)


def build_tools(data,title, top = 6, percentage: bool = True, time: bool = False):
    return f"""### {title} ({data['human_readable_total']})
- **Languages**: {format_waka_list(data['languages'][0:top], percentage=percentage, time = time)}
- **Editors**: {format_waka_list(data['editors'][0:top], percentage=percentage, time = time)}
- **Operating Systems**: {format_waka_list(data['operating_systems'][0:top], percentage=percentage, time = time)}
    """

# https://github.com/alexandresanlim/Badges4-README.md-Profile

out(
    f"""
### Hello There! I'm Thomas Kwashnak

Undergraduate Student at Quinnipiac University studying Computer Science and Data Science, with a minor in economics.

You can see more on my personal website! [littletealeaf.github.io](https://littletealeaf.github.io). 

{build_tools(waka_weekly,"Last Week", percentage = False, time = True)}

*auto-generated using python. data collected since August 2022*
"""
)
