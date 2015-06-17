# coding:utf-8
"""
python knock067.py 
"""

import sys
from pymongo import Connection

# connection
connect = Connection('localhost', 37017)
db = connect['100knock']
collect = db['064']

for line in iter(sys.stdin.readline, '\n'):
    datas = collect.find({"aliases.name": line.strip()})
    if datas:
        for data in datas:
            print data
    else:
        print "None"
