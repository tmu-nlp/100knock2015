#!usr/bin/python
#coding:utf-8

import re

def main():
    re_pattern = re.compile('<word>(.+?)</word>')
    re_lemma = re.compile('<lemma>(.+?)</lemma>')
    re_pos = re.compile('<POS>(.+?)</POS>')
    word_list = list()
    lemma_list = list()
    pos_list = list()
    for line in open('nlp.txt.xml'):
        word_result = re_pattern.search(line)
        lemma_result = re_lemma.search(line)
        pos_result = re_pos.search(line)
        if word_result is not None:
            word_list.append(word_result.group(1))
        if lemma_result is not None:
            lemma_list.append(lemma_result.group(1))
        if pos_result is not None:
            pos_list.append(pos_result.group(1))
    for word,lemma,pos in zip(word_list,lemma_list,pos_list):
        print word +'\t'+lemma+'\t'+pos



if __name__ == '__main__':
    main()

