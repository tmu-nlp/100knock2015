#!/usr/bin/python
# coding:utf-8

import plyvel

def main():
		my_DataBese = plyvel.DB('test.ldb', create_if_missing=True) 
		print my_DataBese.get('黒木メイサ')

if __name__ == '__main__':
    main()