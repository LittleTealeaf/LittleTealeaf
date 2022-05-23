
def code_block(language: str, content: str):
    return f"```{language}\n{content}\n```"

def quote(content: str):
    return "> " + content.replace("\n","\n> ")
