#!/usr/bin/env python
#
# LaunchBar Action Script
#
import subprocess

# networked drivers list
NETWORKED_DRIVES = ['smb://your-domain.com/directory']

for s in NETWORKED_DRIVES:
    server = '"%s"' % s
    cmd = "osascript -e 'try' -e 'mount volume %s' -e 'end try'" % server
    subprocess.call(cmd, shell=True)
