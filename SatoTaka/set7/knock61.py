#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

import plyvel

def main():
    artist_name_db = plyvel.DB("data_base.ldb")
    print artist_name_db.get("黒木メイサ")
    artist_name_db.close()
    

if __name__=="__main__":
   main()
