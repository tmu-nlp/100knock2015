#!usr/bin/python
#coding:utf-8
import plyvel
import json

def level_db():
	encode_jsondict={}
	artist_area = plyvel.DB('artist.ldb', create_if_missing = True)
	for line in open('artist.json'):
		artist_jsondict = json.loads(line)
		artist_area.put(artist_jsondict['name'].encode('utf-8'),artist_jsondict.get('area','NONE').encode('utf-8'))
	return artist_area
if __name__ == "__main__":
	for i,j in level_db():
		print i,j
