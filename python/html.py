def hheader(content,level=1):
    return htag(f"h{level}",content)

def hdetails(summary,content):
    return htag("details",htag("summary",summary) + content)

def himage(source,alt="",style=""):
    return f"<img src=\"{source}\" alt = \"{alt}\" style=\"{style}\">"

def hlist(values,tag="ul"):
    string = "</li><li>".join(values)
    return f"<ul><li>{string}</li></ul>"

def hlink(content,link):
    return htag(f"a href=\"{link}\"",content)

def hline():
    return "<br>"

def htag(a,vals):
    closeTag = a.partition(" ")[0]
    return f"<{a}>{vals}</{closeTag}>"

def hparagraph():
    return "<p>"
