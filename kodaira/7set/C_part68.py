
#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import Connection
import pymongo

if __name__ == "__main__":

    connect = Connection()
    db = connect.nlp100_kodair
    col = db.json_dict
    count = 0
    active_list = ['name', 'tags.value', 'rating.value']
    print 'Ranking  --Dance--'
    for one_dict in col.find({'tags.value':'dance'}) \
        .sort('rating.value', pymongo.DESCENDING):
        count += 1 
        print 'No.' + str(count) + ': ',
        print one_dict[u'name'] + '\n        ' + \
            str(one_dict[u'rating'][u'value'])
        if count == 100:
            break
    
