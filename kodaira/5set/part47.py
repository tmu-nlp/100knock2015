#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *


def get_case_frame(text_chunk_list):
    verb = '動詞'; particle = '助詞'; pos1 = 'サ変接続'
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        get_pattern_flag = False
        sahen_flag = False
        for chunk in sentence_chunk_list:
            get_pattern_flag = False
            particle_phrase = ''

            particle_words = ''
            for num in chunk.srcs:
                num = int(num)
                if chunk.check_phrase_pos(verb) \
                and sentence_chunk_list[num].check_phrase_pos(particle):
                    temp_phrase = sentence_chunk_list[num].get_phrase()
                    if sentence_chunk_list[num].check_phrase_pos1(pos1) \
                        and sentence_chunk_list[num].check_phrase_word('を'):
                        sahen_phrase = temp_phrase
                        sahen_flag = True
                    else:
                        particle_phrase += temp_phrase
                    particle_words += str(sentence_chunk_list[num].get_pos_word(particle) )
                    particle_phrase += ' '

                    get_pattern_flag = True
                    check_print = True
            if get_pattern_flag and sahen_flag:
                print sahen_phrase + chunk.get_pos_word(verb), '\t', \
                    particle_words, '\t', particle_phrase

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_case_frame(text_chunk_list)
