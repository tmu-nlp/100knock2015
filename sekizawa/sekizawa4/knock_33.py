#!usr/bin/python
#coding:utf-8

if __name__ == "__main__":


    f = open("neko.txt.mecab", "r")

    for line in f:
        line = line.strip().replace(" ", "")
        line = unicode(line, "utf-8")
        words = line.split(",")
        word = words[3].encode("utf-8")

        if word == "サ変可能" and len(words) > 9:
            print words[8].encode("utf-8")
            

    f.close()

