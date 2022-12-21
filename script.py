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


def build_tools(data,title, top = 6,):
    return f"""### {title} ({data['human_readable_total']})
- **Languages**: {format_waka_list(data['languages'][0:top], percentage=True)}
- **Editors**: {format_waka_list(data['editors'][0:top], percentage=True)}
- **Operating Systems**: {format_waka_list(data['operating_systems'][0:top], percentage=True)}
    """


out(
    f"""
### Hello There! I'm Thomas Kwashnak

- Undergraduate Student at Quinnipiac University studying Computer Science and Data Science, with a minor in economics.
- Not currently looking for a job, but wide open for internship opportunities for Summer 2023

You can see more on my personal website! [littletealeaf.github.io](https://littletealeaf.github.io). Fair warning! I'm still finding time to finish up my website, so there's not much there yet.

{build_tools(waka_weekly,"Last Week")}
{build_tools(waka_monthly,"Last Month")}
{build_tools(waka_all,"All Time")}

*auto-generated using python.*
"""
)
