#!usr/bin/python
#coding:utf-8

if __name__ == "__main__":

    f = open("neko.txt.mecab", "r")
    noun = []

    for line in f:
        line = line.strip().replace(" ", "")
        line = unicode(line, "utf-8")
        words = line.split(",")

        if words[1].encode("utf-8") == "名詞":
            noun.append(words[0].encode("utf-8"))

        elif len(noun) > 0:
            for word in noun:
                print word,
            print "\n"
            noun = []

    f.close()


