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

table = "|Name|Description|License|\n"
table += "|--|--|--|\n"
for editor in editors:
    license = editor["license"]
    badge_license = shields_component(license)
    table += "| [" + editor["name"] + "](" + editor["link"] + ") "
    table += "| " + editor["description"]
    table += f"| ![License: {license}]"
    table += f"(https://img.shields.io/badge/license-{badge_license}-006060)"
    table += " |\n"

with open("./Readme.src.md", "r") as file:
    content = file.read();
    content = content.replace("# Editors", table)
    with open("./Readme.md", "w") as out:
        out.write(content)