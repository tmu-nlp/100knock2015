#!usr/bin/python
#coding:utf-8

if __name__ == "__main__":

    f = open("neko.txt.mecab", "r")
    flag = 0

    for line in f:
        line = line.strip().replace(" ", "")
        line = unicode(line, "utf-8")
        words = line.split(",")

        if flag == 0 and words[1].encode("utf-8") == "名詞":
            ext1 = words[0].encode("utf-8")
            flag += 1
        elif flag == 1 and words[0].encode("utf-8") == "の":
            ext2 = words[0].encode("utf-8")
            flag += 1
        elif flag == 2 and words[1].encode("utf-8") == "名詞":
            ext3 = words[0].encode("utf-8")
            flag -= 2
            print ext1 + ext2 + ext3
        else:
            flag == 0

    f.close()

