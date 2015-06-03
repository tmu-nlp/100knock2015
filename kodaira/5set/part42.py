#!/usr/bin/python
#coding:utf-8

# make kakariuke  this class has morphs, dst, srcs
from part41 import *



def get_kakari_pair(text_chunk_list):
    for sentence_chunk_list in text_chunk_list:
        for chunk in sentence_chunk_list:
            if chunk.dst != '-1':
                print chunk.get_phrase(), '\t', \
                    sentence_chunk_list[int(chunk.dst)].get_phrase()
        print ''


if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_kakari_pair(text_chunk_list)
