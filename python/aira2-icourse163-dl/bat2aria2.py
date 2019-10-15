import re

source = "BAT FILE"
output = "OUTPUT FILE FOR ARIA2"
download_dir = "VIDEO FOLDER"

download_list_file = open(source, "r", encoding='gbk')
# print(download_list.read())

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
