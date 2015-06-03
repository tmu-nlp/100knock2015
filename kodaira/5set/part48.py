#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *

def print_noun_to_root(sentence_chunk_list, noun_phrase,  dst):
    print noun_phrase,
    while dst != '-1':
        print '-> ' + sentence_chunk_list[int(dst)].get_phrase(),
        dst = sentence_chunk_list[int(dst)].dst
    print ''



def get_trace_pass(text_chunk_list):
    noun = '名詞'
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        for chunk in sentence_chunk_list:
            if chunk.check_phrase_pos(noun) and chunk.dst != '-1':
                noun_phrase = chunk.get_phrase()
                print_noun_to_root(sentence_chunk_list, noun_phrase, chunk.dst)
        print '' 
                

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_trace_pass(text_chunk_list)
