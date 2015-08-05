#!/usr/bin/python
# coding:utf-8

import plyvel
import json
import sys


def KVS(artist_file):
	my_DataBese = plyvel.DB('test.ldb', create_if_missing=True) 
	for line in artist_file:
		jdict = json.loads(line.strip())
		my_DataBese.put(jdict["name"].encode('utf-8'),jdict.get("area","null").encode('utf-8'))
	
	#return my_DataBese

	for key, value in my_DataBese:
		print key,value

def main(jsonfile):
	KVS(jsonfile)

if __name__ == '__main__':
    main(open(sys.argv[1]))