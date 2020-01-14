import os
import re
import shutil
import json

DIR = ""

empty_dir_deletion_queue = []
# list all items in DIR
for i in os.listdir(DIR):
    path = os.path.join(DIR, i)
    # detect empty dirs
    if os.path.isdir(path):
        path_subfiles = os.listdir(path)
        no_hide_files = []
        for f in path_subfiles:
            if not re.search(r"^\..*", f):
                no_hide_files.append(f)
        if len(no_hide_files) == 0:
            empty_dir_deletion_queue.append({
                "name": i,
                "path": path
            })

items = []
if len(empty_dir_deletion_queue):
    for t in empty_dir_deletion_queue:
        shutil.rmtree(t["path"])
        items.append({
            "title": "%s ... removed" % t["name"],
            "icon": "folder.png"
        })
else:
    items.append({
        "title": "Congrats! There is nothing to remove.",
        "icon": "done.png"
    })

print(json.dumps(items))
