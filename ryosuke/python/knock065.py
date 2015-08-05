# coding:utf-8
"""
python knock065.py 
"""

from pymongo import Connection

# connection
connect = Connection('localhost', 37017)
db = connect['100knock']
collect = db['064']

for data in collect.find({'name': 'Queen'}):
    print data
