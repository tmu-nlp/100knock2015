#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import MongoClient
import pymongo

if __name__ == "__main__":

    client = MongoClient('localhost', 27017)
    db = client.nlp100
    col = db.json_dict
    count = 0
    active_list = ['name', 'tags.value', 'rating.value']
    print 'Ranking  --Dance--'
    for one_dict in col.find({'tags.value':'dance'}).sort('rating.count', pymongo.DESCENDING):
        count += 1 
        print 'No.' + str(count) + ': ',
        print one_dict[u'name'] + '\n        ' + \
            str(one_dict[u'rating'][u'count'])
        if count == 100:
            break
    
