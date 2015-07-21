#!usr/bin/local/python
#coding:utf-8

import kyotocabinet as kc
import knock_60

if __name__ == "__main__":
    count = 0
    db = knock_60.KyotoCabinet()
    db.open("artist.kch", kc.DB.OWRITER | kc.DB.OCREATE)
    for key in db:
        if db[key] == "Japan":
            count += 1
    print count


