
#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import Connection


if __name__ == "__main__":

    connect = Connection()
    db = connect.nlp100_kodair
    col = db.json_dict
    print "area: japan:  ", col.find({'area':'Japan'}).count()
    
