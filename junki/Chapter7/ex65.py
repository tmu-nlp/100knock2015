#!usr/bin/python
#-*-coding:utf-8-*-

from pymongo import MongoClient

def main():
	client = MongoClient("localhost",27017)
	database = client.test#
	collection = database.artist
	print database.name

	#for data in collection.find({'name':'Queen'}):
	for data in collection.find():

		print data

if __name__ == '__main__':
	main()