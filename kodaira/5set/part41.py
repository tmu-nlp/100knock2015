#!/usr/bin/python
#coding:utf-8

# make Chunk class . this class has surface, base, pos, pos1

from part40 import Morph
from collections import defaultdict
import sys
class Chunk:
    symbol_list = ['「', '」', '（', '）', '、', '。']
    def __init__(self,  dst, num, srcs):
        self.dst = dst
        self.srcs = srcs
        self.morphs = []
        self.num = num

    def append_morph(self, mecab_result):
        self.morphs.append(Morph(mecab_result) )
    

    def to_string(self):
        string = ''
        for morph in self.morphs:
            string += morph.surface
        return string + '\t' + self.dst + '\t' + ','.join(self.srcs) 

    def get_phrase(self):
        phrase = ''
        for morph in self.morphs:
            if morph.surface in self.symbol_list:
                continue
            phrase += morph.surface
        return phrase

    def check_phrase_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_pos_word(self, pos):
        phrase = ''
        for morph in self.morphs:
            if morph.pos == pos:
                if pos == '助詞':
                    phrase += morph.surface + ' '
                elif pos == '動詞':
                    phrase += morph.base
                    break
        return phrase

    def check_phrase_pos1(self, pos1):
        for morph in self.morphs:
            if morph.pos1 == pos1:
                return True
        return False
    def check_phrase_word(self, word):
        for morph in self.morphs:
            if morph.surface == word:
                return True
        return False
    
    def phrase_replace(self, pos, re_word):
        phrase = ''
        for morph in self.morphs:
            if morph.surface in self.symbol_list:
                continue
            if morph.pos == pos:
                if not re_word in phrase:
                    phrase += re_word
            else:
                phrase += morph.surface
        return phrase

    def root_word(self, sentence_chunk_list, dst):
        word_dst = dst
        while word_dst != '-1':
            word_dst = sentence_chunk_list[word_dst].dst
        return sentence_chunk_list[word_dst].get_phrase()


def make_text_chunk():
    text_chunk_list = []
    sentence_chunk_list = []
    srcs_dict = defaultdict(list)
    count = 0
    for line in open(sys.argv[1]):
        if line[:3] == 'EOS':
            count = 0
            text_chunk_list.append(sentence_chunk_list)
            srcs_dict = defaultdict(list)
            sentence_chunk_list = []

        elif line[:2] == '* ':
            chunk_info = line.strip().split(' ')
            chunk_info[2] = chunk_info[2].rstrip('D')
            srcs_dict[chunk_info[2]]
            phrase_chunk = Chunk(chunk_info[2], \
                count, srcs_dict[chunk_info[1]])
            srcs_dict[chunk_info[2] ].append(chunk_info[1])
            sentence_chunk_list.append(phrase_chunk)
            count += 1
        else:
            # line is mecab analysis result
            phrase_chunk.morphs.append(Morph(line) )
    return text_chunk_list





if __name__ == '__main__':
   text_chunk_list = make_text_chunk()
   count = 0
   for sentence_chunk_list in text_chunk_list:
       count += 1
       for chunk in sentence_chunk_list:
           if count == 8:
               print chunk.to_string()
