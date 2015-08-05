#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *
def root_word( sentence_chunk_list, dst):
     word_dst = dst
     prev_dst = int(dst)
     while sentence_chunk_list[int(word_dst)].dst != '-1':
         word_dst = int(word_dst)
         prev_dst = word_dst
         word_dst = sentence_chunk_list[word_dst].dst
     return sentence_chunk_list[prev_dst].get_phrase()

def print_noun_to_root(sentence_chunk_list, noun_phrase,  dst):
    print noun_phrase,
    while dst != '-1':
        print '-> ' + sentence_chunk_list[int(dst)].get_phrase(),
        dst = sentence_chunk_list[int(dst)].dst


def make_phrase_list(sentence_chunk_list, noun_phrase,  dst):
    phrase_list = list()
    phrase_list.append(noun_phrase)
    while sentence_chunk_list[int(dst)].dst != '-1':
        phrase_list.append(sentence_chunk_list[int(dst)].get_phrase() )
        dst = sentence_chunk_list[int(dst)].dst
    return phrase_list

def check_same_phrase(phrase_list1, phrase_list2):
    for phrase in phrase_list1:
        if phrase in phrase_list2:
            return True, phrase

    return False, 'NULL'



def make_minimum_pass(sentence_chunk_list, noun_num_list):
    particle = '助詞'; noun = '名詞'
    match_flag = False
    count = 0
    sub_noun_num_list = list(noun_num_list)
    for phrase_num in noun_num_list:
        count += 1
        sub_noun_num_list.remove(phrase_num)
        chunk = sentence_chunk_list[phrase_num]
        first_word =  chunk.phrase_replace(noun, 'X')
        top_phrase_list = make_phrase_list(sentence_chunk_list, \
            chunk.get_phrase(), chunk.dst)
        for other_num in sub_noun_num_list:
            next_chunk = sentence_chunk_list[other_num]
            next_phrase_list = make_phrase_list(sentence_chunk_list, \
                next_chunk.get_phrase(), next_chunk.dst)
            match_flag, match_num = check_same_phrase(top_phrase_list, \
                    next_phrase_list[:-1])
            print first_word,
            if match_flag:
                print ' -> ' + ' -> '.join(next_phrase_list[:-1]) +  ' -> Y'
            else:
                print ' | ',
                print_noun_to_root(sentence_chunk_list, \
                        next_chunk.phrase_replace(noun, 'Y'), next_chunk.dst)
                print ' | ' + root_word(sentence_chunk_list, chunk.dst)
        

        

def make_noun_num_list(sentence_chunk_list):
    noun_num_list = list()
    noun = '名詞'
    for chunk in sentence_chunk_list:
        if chunk.check_phrase_pos(noun):
            noun_num_list.append(chunk.num)
    return noun_num_list

def get_trace_pass(text_chunk_list):
    for sentence_chunk_list in text_chunk_list:
        check_print = False

        noun_num_list = make_noun_num_list(sentence_chunk_list)
        if noun_num_list != []:
            make_minimum_pass(sentence_chunk_list, noun_num_list)

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_trace_pass(text_chunk_list)
