
#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import MongoClient
import pymongo
from bottle import route, run, template, request
from types import *


def get_info(data_dict):
    infos = ''
    for tag, info in data_dict.items():
        if type(info) is ListType:
            infos += str(tag) + '\n'
            for tag2, info2 in info[0].items():
                infos += ' ' + str(tag2) + str(info2) + '/n'
        elif type(info) is DictType:
            infos += str(tag) + '\n'
            for tag2, info2 in info.items():
                infos += ' ' + str(tag2) + str(info2) + '\n'
        else:
            if info == True or tag == '_id':
                continue
            if type(info) is IntType:
                info = unicode(info)
            infos += str(tag) + str(info) + '/n'
        
    print type(infos)
    return infos + '/n'


client = MongoClient('localhost', 27017)
db = client.nlp100
col = db.json_dict
@route("/")
def docroot():
  query_tag = ['name', 'aliases.name', 'tags.value']
  query_dict = dict()
  query_list = [request.query.name, request.query.aliases_name, request.query.tags_value]
  for tag, query in zip(query_tag, query_list):
      if query:
          query_dict[tag] = query
  ans = list()
  search_result = list()

  return template("root", result = col.find(query_dict).sort('rating.count', pymongo.DESCENDING), query =  query_dict )

run(host = "localhost", port = 8080, debug = True, reloader = True)
