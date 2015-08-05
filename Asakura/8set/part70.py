#!usr/bin/python
#coding:utf-8

import random

def main():
    neg_file = open('rt-polaritydata/rt-polaritydata/rt-polarity.neg')
    pos_file = open('rt-polaritydata/rt-polaritydata/rt-polarity.pos')
    new_file = open('sentiment.txt','w')
    pos_list = []
    neg_list = []
    for neg_line,pos_line in zip(neg_file,pos_file):
        neg_sentence = '-1 '+neg_line
        pos_sentence = '+1 '+pos_line
        neg_list.append(neg_sentence)
        pos_list.append(pos_sentence)

    neg_list.extend(pos_list)
    random.shuffle(neg_list)
    for line in neg_list:
        new_file.write(line)

    neg_file.close()
    pos_file.close()
    new_file.close()

if __name__ == '__main__':
    main()
