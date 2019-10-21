# coding: utf-8
# author: xavierniu
# a tool for downloading videos from iCourse163.com by Aria2

import re
import subprocess
import os

HOME = os.path.expanduser('~')

source = "%s/Downloads/xxx.bat" % HOME
output = "%s/Downloads/icourse163.aria2" % HOME
download_dir = "%s/Downloads" % HOME
# aria2 conf
ARIA2_CONF_PATH = "%s/.aria2/aria2.conf" % HOME

download_list_file = open(source, "r", encoding='gbk')

download_str = download_list_file.read()
download_list = download_str.split(" & ")[:-1]

aria2_download_file = open(output, "w")

for i in download_list:
    url = re.search(r'(?<=wget\ \").*(?=\"\ -O)', i)
    name = re.search(r'(?<=\ -O\ \").*(?=\")', i)
    # print(i)
    url = url.group(0)
    name = name.group(0)
    # inspect the name whether constains '/' that may create a sub-folder unexpectedly
    # for example: 'I/O' -> 'I-O'
    name = re.sub(r'/', '-', name)
    aria2_download_file.write("%s\n" % url)
    aria2_download_file.write("  dir=%s\n" % download_dir)
    aria2_download_file.write("  out=%s\n" % name)

download_list_file.close()
aria2_download_file.close()

print("🌟🌟🌟 Download file of videos for Aria2 is created successfully at %s" % output)
print("🌟🌟🌟 Total: %d videos" % len(download_list))

subprocess.call("aria2c --conf-path='%s' -i '%s'" % (ARIA2_CONF_PATH, output), shell=True)
