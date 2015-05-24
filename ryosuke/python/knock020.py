# coding:utf-8
'''
python knock020.py ../Data/jawiki-country.json
'''

import json
import sys

for line in open(sys.argv[1]):
    jdata = json.loads(line)
    if jdata['title'] == u'イギリス':
        print jdata['text']
        break
