import json

def get_editors():
    with open("./editors.js", "r") as file:
        content = file.read();
        content = content.replace("let data = ", "")
        # remove trailing semicolon, plus one for null character
        content = content[:-2]
        return json.loads(content)

editors = get_editors()

list = ""
for editor in editors:
    list += "- [" + editor["name"] + "](" + editor["link"] + ") - "
    list += editor["description"] 
    list += "<kbd>" + editor["license"] + "</kbd>"
    list += "\n"

with open("./Readme.src.md", "r") as file:
    content = file.read();
    content = content.replace("# Editors", list)
    with open("./Readme.md", "w") as out:
        out.write(content)