#!usr/bin/python
#coding:utf-8


import plyvel

def main():
    my_db = plyvel.DB('test.1db',create_if_missing=False)
    area = my_db.get('Jim Jidhed'.encode('utf-8'))
    print area




if __name__=='__main__':
    main()
