# coding: utf-8
# author: xavier niu
# a tool for renamer for icourse163 video parsed by antlm.com

import re
import subprocess
import os

HOME = os.path.expanduser('~')

LINK_SOURCE = '%s/Downloads/download_link.txt' % HOME
# VIDEO_FOLDER has no separator at the end
VIDEO_FOLDER = '%s/Downloads/xxx' % HOME

parsing_counter = 0
error_list = []
name_map = []

with open(LINK_SOURCE, 'r') as file:
    for l in file.readlines():
        downloaded_name = re.search(r'(?<=\/\d{4}\/\d{2}\/\d{2}\/).*(?=\+\|\+)', l)
        real_name = re.search(r'(?<=\+\|\+).*$', l)
        if downloaded_name is not None and real_name is not None:
            # replace invalid charactors with valid one
            rn = re.sub(r'/', '-', real_name.group(0))
            rn = re.sub(r' ', '\ ', rn)
            name_map.append({
                'dn': downloaded_name.group(0),
                'rn': rn
            })
            parsing_counter += 1
        else:
            error_list.append(l)

print('🌟🌟🌟 success: %d, error: %d.' % (parsing_counter, len(error_list)))
print('🌟🌟🌟 parsing errors: ')
for e in error_list:
    print('\t %s' % e)

for l in name_map:
    print(l['dn'], l['rn'])
    subprocess.call("mv %s%s%s.mp4 %s%s%s.mp4" % (VIDEO_FOLDER, os.altsep, l['dn'], VIDEO_FOLDER, os.altsep, l['rn']), shell=True)