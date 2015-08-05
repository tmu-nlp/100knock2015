#!usr/bin/python
#-*-coding:utf-8-*-
import plyvel

def main():
	count = 0
	my_DataBese = plyvel.DB('test.ldb', create_if_missing=True) 
	for key, value in my_DataBese:
		if value == 'Japan':
			print key,value
			count += 1
	print '総アーティスト数'+str(count)

if __name__ == '__main__':
    main()