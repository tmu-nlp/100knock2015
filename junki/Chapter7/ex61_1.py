#!/usr/bin/python
# coding:utf-8

import plyvel
import json
import sys


def main():
		my_DataBese = plyvel.DB('test.ldb', create_if_missing=True) 
		print my_DataBese.get(sys.argc[1])

if __name__ == '__main__':
    main()