
#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import Connection
from types import *

def print_db_info(data_dict):
    for tag, info in data_dict.items():
        if type(info) is ListType:
            print tag
            for tag2, info2 in info[0].items():
                print ' ', tag2, info2
        elif type(info) is DictType:
            print tag
            for tag2, info2 in info.items():
                print ' ', tag2, info2
        else:
            print tag, info
    print '\n'  

if __name__ == "__main__":

    connect = Connection()
    db = connect.nlp100_kodair
    col = db.json_dict
    for data_dict in col.find({'name':'Queen'}):
        print_db_info(data_dict)
