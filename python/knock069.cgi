#!/usr/bin/python
# coding:utf-8
"""
python knock069.py 
"""

import cgi
from pymongo import Connection

print "Content-Type: text/html\n\n"
# get form info
form = cgi.FieldStorage()
query = dict()
if form.has_key('name'):
    query['name'] = form['name'].value
if form.has_key('aliases_name'):
    query['aliases.name'] = form['aliases_name'].value
if form.has_key('tag'):
    query['tags.value'] = form['tag'].value
if not query.keys():
    print 'Ther is no query'
    exit()

# connection
connect = Connection('fomalhaut', 30000)
db = connect['100knock2015']
collect = db['artist']

# find
data = collect.find(query)
if data:
    for i, doc in enumerate(sorted(filter(lambda d: 'rating' in d, data), key=lambda x: -x['rating']['count'])[:10]):
        print i+1
        print doc
        print
else:
    print 'Thre is no Artist'
