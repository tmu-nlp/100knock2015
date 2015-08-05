# coding:utf-8
"""
python knock068.py 
"""

import sys
from pymongo import Connection

# connection
connect = Connection('localhost', 37017)
db = connect['100knock']
collect = db['064']

data = collect.find({'tags.value': 'dance'})
if data:
    for i, doc in enumerate(sorted(filter(lambda d: 'rating' in d, data), key=lambda x: -x['rating']['count'])[:10]):
        print i+1
        print doc
        print
else:
    print 'None'
