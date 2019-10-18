#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

items = []
languages = ["zh", "en"]
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    for language in languages:
        my_command = ["trans", "-brief", ":"+language, arg]
        content = sp.check_output(my_command, env=my_env)
        content = content.decode("utf-8")
        item = {}
        item["title"] = content[:-1]
        item["icon"] = language+"_flag.png"
        items.append(item)
print(json.dumps(items))
