#!usr/bin/python
#coding:utf-8
import plyvel
from knock60 import level_db

def artist_area(artist):
	artist_place = []
	for i,j in level_db():
		if i == artist:
			artist_place.append(j)
	return artist_place
if __name__ == '__main__':
	for i in artist_area('浜崎あゆみ'):
		print i
