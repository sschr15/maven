#!user/bin/python
# because even though I might not run Linux,
# it still should be available to the public.

from typing import Dict, List
import json
import os

run = os.system
recursive_dict = Dict[str, List[str]]

json_struct: recursive_dict = {}

for root, folders, files in os.walk("."):
    root: str = root.replace("\\", "/")
    folders: List[str] = [i for i in folders if not i.startswith(".")]
    files: List[str] = [i for i in files if not i.startswith(".")]

    if root.startswith("./.git"):
        continue
    if (root == "."):
        files = []

    json_struct[root] = folders + files

with open("tree.json", "w") as json_file:
    json.dump(json_struct, json_file)

run("git add .")
run('git commit -m "Auto-commited by script"')
run("git push")
