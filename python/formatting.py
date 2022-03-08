import json


def html_header(content,level=1):
    return html_tag(f"h{level}",content)

def html_details(summary,content):
    return html_tag("details",html_tag("summary",summary) + content)

def html_list(values,tag="ul"):
    return html_tag(tag,html_tag("li","</li><li>".join(values)))

def html_link(content,link):
    return html_tag("a",content,{'href': link })

def html_img(src,alt="",style=""):
    return f"<img src=\"{src}\" alt=\"{alt}\" style=\"{style}\">"

def html_tag(tag,value,attributes={}):
    attribute_string = " ".join([f"{item}=\"{attributes[item]}\"" for item in attributes])
    return f"<{tag} {attribute_string}>{value}</{tag}>"

def markdown_codeblock(code,style=""):
    return f"```{style}\n{code}\n```"

def markdown_pretty_json(data):
    return markdown_codeblock(json.dumps(data,indent=4,sort_keys=False),'json')