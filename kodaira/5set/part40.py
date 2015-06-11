#!/usr/bin/python
#coding:utf-8

# make Morph class 

import sys
# Morph has mecab analysis result (pos, surface, base)
class Morph : 
     
    # stores received mecab analysis result
    def __init__(self, mecab_result):
        result = mecab_result.replace('\t', ',').split(',')
        self.surface = result[0]
        self.base = result[7]
        self.pos = result[1]
        self.pos1 = result[2]
        

    # return variables in Morph 
    def to_string(self):
      strin = 'surface:%s\t base:%s\t pos:%s\tpos1:%s\t' % (self.surface, self.base, self.pos, self.pos1) 
      return  strin


def make_text_morphs():
    sentence_morph_list = []
    text_morph_list = []

    for line in open(sys.argv[1]):
        if line[0] == '*':
            continue
        elif line[0:3] == 'EOS':
            text_morph_list.append(sentence_morph_list)
            sentence_morph_list = []
        else:
            sentence_morph_list.append(Morph(line) )

    return text_morph_list


if __name__ == '__main__':
    text_morph_list = make_text_morphs()
    for morph in text_morph_list[2]:
        print morph.to_string()
