def table(headers, content, spacing=None):
    headers_str = " | ".join(headers)
    spacing_str = " | ".join(
        spacing if spacing is not None else len(headers) * [":---:"])

    rows = []
    for row in content:
        cells = " | ".join(row)
        rows.append(f"| {cells} |")

    body = "\n".join(rows)

    return f"| {headers_str} |\n| {spacing_str} |\n{body}"
