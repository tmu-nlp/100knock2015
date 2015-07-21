#!usr/local/bin/python
#coding:utf-8

import kyotocabinet as kc
import knock_60

if __name__ == "__main__":
    db = knock_60.KyotoCabinet()
    db.open("artist.kch", kc.DB.OWRITER | kc.DB.OCREATE)
    print(db.get_str(u"Aylen"))

