import subprocess
import time
import os

GIT_REPO = ""
# As default, commit message is like "Python Auto Commit at 2019-10-19 00:06:16"
COMMIT_MESSAGE = "Python Auto Commit at %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

subprocess.call('git add --all && git commit -a -m "%s" && git push' % COMMIT_MESSAGE, cwd=GIT_REPO, shell=True, executable='/bin/zsh')

subprocess.call("terminal-notifier -title 'Blog Backup' -message 'Backup Successful!' -sound 'default' -ignoreDnD", shell=True, executable='/bin/zsh', env=my_env)