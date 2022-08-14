import json
import string
from libs.cache import clean_cache
import libs.github as github
from libs.markdown import *
from libs.util import *
import libs.wakatime as wakatime

clean_cache()

def out(content: str):
    with open("README.md",'w') as file:
        file.write(content)

user = github.getREST("https://api.github.com/users/LittleTealeaf")


waka_stats = wakatime.getData('/api/v1/users/LittleTealeaf/stats/all_time')['data']
waka_recent = wakatime.getData('/api/v1/users/LittleTealeaf/stats/last_30_days')['data']

top_languages = waka_stats['languages'][0:5]
top_languages_recent = waka_recent['languages'][0:5]

def format_language(language,time = True):git a
    name = language['name']
    text = language['text'] if time else f"{language['percent']}%"
    return f'{name} - {text}'

top_languages_print = [format_language(language,time=False) for language in top_languages]
top_languages_recent_print = [format_language(language,time=True) for language in top_languages_recent]


top_projects_recent = waka_stats['projects'][0:5]
for project in top_projects_recent:
    project_data = wakatime.getData(f'/api/v1/users/LittleTealeaf/projects/{project["name"]}')['data']
    if 'repository' in project_data and project_data['repository'] != None:
        project_github_api = github.getREST(project_data['repository']['url'])
        project['github_api'] = project_github_api
    project['project_api'] = project_data

def format_recent_project(project):
    name = project["name"]
    if 'github_api' in project:
        url: str = project['github_api']['html_url']
        # name = f'[{project["github_api"]["full_name"]}]({url})'
        name = f'<a href="{url}">{project["github_api"]["full_name"]}</a>'
    time_in_last_7_days = project['text']

    return f'{name} - {time_in_last_7_days}'

print_project_list = [format_recent_project(project) for project in top_projects_recent]

aboutme = code_block('json',json.dumps(load_json('config/aboutme.json'),indent=4))

stats = ""

out(f"""
{aboutme}

<details><summary>Recent Projects (Last 7 days)</summary>
<ul><li>{
    '</li><li>'.join(print_project_list)
}</li></ul></details>

<details><summary>Top Recent Languages</summary>
<ul><li>{
    '</li><li>'.join(top_languages_recent_print)
}</li></ul></details>

<details><summary>Top All-Time Languages</summary>
<ul><li>{
    '</li><li>'.join(top_languages_print)
}</li></ul></details>

*made with python*
""")
