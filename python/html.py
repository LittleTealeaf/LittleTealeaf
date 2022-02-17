def html_header(content,level=1):
    return html_tag(f"h{level}",content)

def html_details(summary,content):
    return html_tag("details",html_tag("summary",summary) + content)

def html_img(source,alt="",style=""):
    return f"<img src=\"{source}\" alt = \"{alt}\" style=\"{style}\">"

def html_list(values,tag="ul"):
    """
    Creates an HTML List from contents
    """
    string = "</li><li>".join(values)
    return f"<ul><li>{string}</li></ul>"

def html_link(content,link):
    
    return html_tag(f"a href=\"{link}\"",content)

def html_line():
    return "<br>"

def html_tag(a,vals):
    closeTag = a.partition(" ")[0]
    return f"<{a}>{vals}</{closeTag}>"
