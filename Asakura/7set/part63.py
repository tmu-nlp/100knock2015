#!usr/bin/python
#coding:utf-8

import plyvel
import json
import pickle

def main():
    my_db = plyvel.DB('test.2db',create_if_missing=True)
    for line in open('artist.json'):
#   for line in open('artist_small.json'):
        jdata = json.loads(line.strip())
#        if u'tags' not in my_db:
#            continue
        try:
            tag_list = pickle.dumps(jdata[u'tags'])
            my_db.put(jdata[u'name'].encode('utf-8'), tag_list)
        except(KeyError):
            pass
    for key,value in my_db:
        print key+'\t',
        for dic in pickle.loads(value):
            for key2,value2 in dic.items():
                print str(key2),
                try:
                    print value2 if isinstance(value2, int) else value2.encode("utf-8"),
                except(UnicodeEncodeError):
                    print "can't encode. Why!!!!!", key, "aaaaaaaaaaaaaaaaaaaaaa"
                print '\t',
        print ''

if __name__ == '__main__':
    main()
