# coding: utf-8
# author: xavier niu
# a tool for renamer for icourse163 video parsed by antlm.com

import re
import subprocess
import os

HOME = os.path.expanduser('~')

LINK_SOURCE = '%s/Downloads/download_link.txt' % HOME
# VIDEO_FOLDER has no separator at the end
VIDEO_FOLDER = '%s/Downloads' % HOME

parsing_counter = 0
error_list = []
name_map = []
manual_handle_list = []

with open(LINK_SOURCE, 'r') as file:
    for l in file.readlines():
        downloaded_name = re.search(r'(?<=\/\d{4}\/\d{2}\/\d{2}\/)(.*)(?=\.\w{3,4}\+\|\+)', l)
        extension = re.search(r'(?<=\.)\w{3,4}(?=\+\|\+)', l)
        real_name = re.search(r'(?<=\+\|\+).*$', l)
        if downloaded_name is not None and real_name is not None and extension is not None:
            # handle escaped characters
            # after renamed you should find and replace "ECF8_E9hfueEC" with "/" manually
            # the list will be shown up at the end part of this execution with prompt of "Files you should rename manually(ECF8_E9hfueEC -> /):"
            rn = re.sub(r'/', 'ECF8_E9hfueEC', real_name.group(0))
            if rn != real_name.group(0):
                manual_handle_list.append(rn)
            # handle m3u8
            dn = downloaded_name.group(0)
            ext = extension.group(0)
            if ext == 'm3u8':
                dn = dn + '.m3u8'
                ext = 'mp4'
            name_map.append({
                'dn': dn,
                'rn': rn,
                'ext': ext
            })
            parsing_counter += 1
        else:
            error_list.append(l)

for l in name_map:
    cmd = "mv \"%s%s%s.%s\" \"%s%s%s.%s\"" % (VIDEO_FOLDER, os.sep, l['dn'], l['ext'], VIDEO_FOLDER, os.sep, l['rn'], l['ext'])
    subprocess.call(cmd, shell=True)

print()
print("================ PARSING LOGS ================")
print('Success: %d, error: %d.' % (parsing_counter, len(error_list)))
if len(error_list) > 0:
    print('Errors happened in parsing process: ')
    for e in error_list:
        print('  filename: %s' % e)
if len(manual_handle_list) > 0:
    print('Files you should rename manually(ECF8_E9hfueEC -> /):')
    for l in manual_handle_list:
        print('  filename: %s' % l)