#usr/bin/python
#coding:utf-8

import random

if __name__ == "__main__":
    pos_file = open("rt-polarity.pos", "r")
    neg_file = open("rt-polarity.neg", "r")
    out_file = open("sentiment.txt", "w")

    pos = "+1 "
    neg = "-1 "
    pos_count = 0
    neg_count = 0

    sentence_list = []
    for line in pos_file:
        pos_line = pos + line
        sentence_list.append(pos_line)
    for line in neg_file:
        neg_line = neg + line
        sentence_list.append(neg_line)

    random.shuffle(sentence_list)
    for line in sentence_list:
        out_file.write(line)
        print line
        if line[0] == "+":
            pos_count += 1
        elif line[0] == "-":
            neg_count += 1

    print "pos:%d" % pos_count
    print "neg:%d" % neg_count

    pos_file.close()
    neg_file.close()
    out_file.close()

