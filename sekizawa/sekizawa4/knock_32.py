#!usr/bin/python
#coding:utf-8

import knock_30

if __name__ == "__main__":
    listdic = knock_30.analyze()

    for line in listdic:
        if line["pos"].encode("utf-8") == "動詞":
            print line["base"].encode("utf-8")

