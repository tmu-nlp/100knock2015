#!usr/bin/python
#coding:utf-8
import plyvel
from knock60 import level_db

def artist_area_count(area):
	count = 0
	for i,j in level_db():
		if j == area:
			count += 1
	return count
if __name__ == '__main__':
	print artist_area_count('Japan')
