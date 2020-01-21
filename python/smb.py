#!/usr/bin/env python
#
# LaunchBar Action Script
#
import subprocess

# networked drivers list, e.g. "smb://your-domain.com/directory"
NETWORKED_DRIVES = ['smb://nas.i.nxw.name/downloads', 'smb://nas.i.nxw.name/nas']

for s in NETWORKED_DRIVES:
    cmd = "osascript -e 'try' -e 'mount volume \"%s\"' -e 'end try'" % s
    subprocess.call(cmd, shell=True)
