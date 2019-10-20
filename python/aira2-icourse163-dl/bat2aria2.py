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
    aria2_download_file.write("%s\n" % url)
    aria2_download_file.write("  dir=%s\n" % download_dir)
    aria2_download_file.write("  out=%s\n" % name)

download_list_file.close()
aria2_download_file.close()

subprocess.call("aria2c --conf-path='%s' -i '%s'" % (ARIA2_CONF_PATH, output), shell=True)
