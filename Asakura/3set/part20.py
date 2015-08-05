#!usr/bin/python
#--*--coding:utf-8--*--

import json
import sys

for line in open(sys.argv[1]):
    jdata = json.loads(line)
    if jdata['title'] == u'イギリス':
       print jdata['text'].encode('utf-8')
