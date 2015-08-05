
#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient('localhost', 27017)
    db = client.nlp100
    col = db.json_dict
    print "area: japan:  ", col.find({'area':'Japan'}).count()
    
