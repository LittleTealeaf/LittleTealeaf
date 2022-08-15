
def code_block(language: str, content: str):
    return f"```{language}\n{content}\n```"

def quote(content: str):
    return "> " + content.replace("\n","\n> ")

def bullet_list(content: list[str]):
    return f"<ul>{''.join(f'<li>{item}</li>' for item in content)}</ul>"
