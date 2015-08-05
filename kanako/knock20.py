#!usr/bin/python
#coding: utf-8
import json
import sys

for line in open('jawiki-country.json'):
    json_data = json.loads(line)
    if json_data['title'] == u'イギリス':
       print json_data['text'].encode('utf-8')

