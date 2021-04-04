#!user/bin/python
# because even though I might not run Linux,
# it still should be available to the public.

from typing import Dict, List
import json
import os

run = os.system
recursive_dict = Dict[str, List[str]]

json_struct: recursive_dict = {}

html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>{0} on concernmaven</title>
    </head>
    <body>
        <h1>Index of {0}</h1>
        <ul>
            {1}
        </ul>
    </body>
</html>
"""

def create_element(filename: str) -> str:
    return '<li><a href="./{0}">{0}</a></li>'.format(filename)

for root, folders, files in os.walk("."):
    root: str = root.replace("\\", "/")
    folders: List[str] = [i for i in folders if not i.startswith(".")]
    files: List[str] = [i for i in files if not i.startswith(".")]

    if root.startswith("./.git"):
        continue
    if (root == "."):
        files = []
        root = "./"

    elements = folders + files
    
    with open(root + "/index.html", "w") as file:
        print("Writing index.html to " + root)
        file.write(html_template.format(
                root,
                "\n            ".join([create_element(i) for i in elements])
        ))

with open("tree.json", "w") as json_file:
    json.dump(json_struct, json_file)

run("git pull")
run("git add .")
run('git commit -m "Auto-commited by script"')
run("git push")
