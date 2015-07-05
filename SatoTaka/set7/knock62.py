#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

import plyvel

def main():
    
    kvs_database = plyvel.DB("data_base.ldb")
    count = 0
    for name, area in kvs_database:
        if area == "Japan":
           count += 1
    print count 

if __name__ == "__main__":
   main()
