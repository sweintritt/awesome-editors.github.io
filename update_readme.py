import json

def get_editors():
    with open("./editors.js", "r") as file:
        content = file.read();
        content = content.replace("let data = ", "")
        # remove trailing semicolon, plus one for null character
        content = content[:-2]
        return json.loads(content)

editors = get_editors()

def kbd(value):
    style = "font-size: 0.75em;" \
        "font-family: monospace;" \
        "color: white;" \
        "background-color: rgb(0, 96, 96);" \
        "margin: 5px;"
    return "<kbd style=\"" + style + "\">"+ value + "</kbd>"

list = ""
for editor in editors:
    list += "- [" + editor["name"] + "](" + editor["link"] + ") - "
    list += editor["description"] 
    list += kbd(editor["license"])
    list += "\n"

with open("./Readme.src.md", "r") as file:
    content = file.read();
    content = content.replace("# Editors", list)
    with open("./Readme.md", "w") as out:
        out.write(content)