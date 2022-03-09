import json


def html_header(content,level=1):
    "Prints a header in HTML, uses the current level to indicate what level it is"
    return html_tag(f"h{level}",content)

def html_details(summary,content):
    "Prints the contents in a html drop-down with a summary label"
    return html_tag("details",html_tag("summary",summary) + content)

def html_list(values,outer="ul",inner="li"):
    "Prints items in an HTML list"
    return html_tag(outer,"".join([html_tag(inner,item) for item in values]))

def html_link(content,link):
    "Creates an HTML link with the content and the link"
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