#!usr/bin/python
#-*-coding:utf-8-*-

from pymongo import MongoClient

def main():
	client = MongoClient("localhost",27017)
	database = client.test#
	collection = database.artist

	for data in collection.find({'area':'Japan'}):
		database.artist == 'Japan':
		count += 1
	print count

if __name__ == '__main__':
	main()