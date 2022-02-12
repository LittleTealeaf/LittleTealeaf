def header(content,level=1):
    return f"<h{level}>{content}</h{level}>"

def details(summary,content):
    return f"<details><summary>{summary}</summary>{content}</details>"

def image(source,alt="",style=""):
    return f"<img src=\"{source}\" alt = \"{alt}\" style=\"{style}\">"

def link(content,link):
    return f"<a href=\"{link}\">{content}</a>"

def line():
    return "<br>"

def paragraph():
    return "<p>"
