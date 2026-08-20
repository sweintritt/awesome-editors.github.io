import json
from urllib.parse import quote

def get_editors():
    with open("./editors.js", "r") as file:
        content = file.read();
        content = content.replace("let data = ", "")
        # remove trailing semicolon, plus one for null character
        content = content[:-2]
        return json.loads(content)

editors = get_editors()

def shields_component(value):
    value = value.replace("-", "--").replace("_", "__")
    return quote(value, safe="")

list = ""
for editor in editors:
    license = editor["license"]
    badge_license = shields_component(license)
    list += "- [" + editor["name"] + "](" + editor["link"] + ") - "
    list += editor["description"]
    list += f"![License: {license}]"
    list += f"(https://img.shields.io/badge/license-{badge_license}-006060)"
    list += "\n"

with open("./Readme.src.md", "r") as file:
    content = file.read();
    content = content.replace("# Editors", list)
    with open("./Readme.md", "w") as out:
        out.write(content)