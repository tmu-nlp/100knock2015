#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *


def get_kakari_pair_verb_noun(text_chunk_list):
    verb = '動詞'; noun = '名詞'
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        for chunk in sentence_chunk_list:
            if chunk.check_phrase_pos(noun) and chunk.dst != '-1' \
            and sentence_chunk_list[int(chunk.dst)].check_phrase_pos(verb):
                print chunk.get_phrase(), '\t', \
                    sentence_chunk_list[int(chunk.dst)].get_phrase()
                check_print = True
        if check_print:
            print ''

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_kakari_pair_verb_noun(text_chunk_list)
