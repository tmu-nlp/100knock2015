#coding:utf-8
'''
python knock025.py ../Data/knock020/result
'''

import sys
import re

re_start_info = re.compile('\{\{基礎情報')
re_end_info = re.compile('\}\}')
re_template = re.compile('\|(.+?) = (.+)')
re_ref = re.compile('(.*)(<ref>.*|<ref .*)')

info = dict()
flag = False
for line in open(sys.argv[1]):
    if re_start_info.match(line) is not None:
        flag = True
        continue
    if re_end_info.match(line) is not None:
        break 
    if flag:
        result = re_template.search(line)
        if result is not None:
            key = result.group(1)
            ref = re_ref.search(result.group(2))
            if ref is not None:
                value = ref.group(1)
            else:
                value = result.group(2)
            info[key] = value 

for key, value in sorted(info.items()):
    print '%s = %s' % (key, value)
