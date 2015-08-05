#!usr/bin/python
#coding:utf-8

import plyvel
import json



def main():
    my_db = plyvel.DB('test.1db',create_if_missing=True)

    for line in open('artist.json'):
        jdata = json.loads(line)
        print jdata
        my_db.put(jdata.get(u'name',jdata['name']).encode('utf-8'),jdata.get(u'area', "asakura").encode('utf-8'))
    for key,value in my_db:
        print key+'\t'+value
    my_db.close()
   



if __name__ == '__main__':
    main()
