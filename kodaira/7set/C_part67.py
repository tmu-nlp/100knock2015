
#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
from pymongo import Connection
from new_part65 import *


if __name__ == "__main__":

    connect = Connection()
    db = connect.nlp100_kodair
    col = db.json_dict
    print 'please input aliases name:'
    aliases_name = 'Queen' #raw_input()
    print 'search', aliases_name, '......'
    for one_dict in col.find({'aliases.name':'Queen'}):
        print_db_info(one_dict)
    
