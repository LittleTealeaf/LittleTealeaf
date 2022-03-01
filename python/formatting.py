
def html_header(content,level=1):
    return html_tag(f"h{level}",content)

def html_details(summary,content):
    return html_tag("details",html_tag("summary",summary) + content)

def html_list(values,tag="ul"):
    return html_tag(tag,html_tag("li","</li><li>".join(values)))

def html_link(content,link):
    return html_tag(f"a href=\"{link}\"",content)

def html_tag(a,vals):
    closeTag = a.partition(" ")[0]
    return f"<{a}>{vals}</{closeTag}>"