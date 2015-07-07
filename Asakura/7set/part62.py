#!usr/bin/python
#coding:utf-8:


import plyvel

def main():
    my_db = plyvel.DB('test.1db',create_if_missing=False)
    count = 0
    for key,value in my_db:
        if my_db.get(key) == 'Japan':
            count += 1

    print count




if __name__ == '__main__':
    main()
