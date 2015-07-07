#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
from collections import defaultdict

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst    = dst
        self.srcs   = srcs

    def get_phrase(self):
        phrase = ""
        for morph in self.morphs:
            phrase += morph.surface
        return phrase

    def check_base(self, base):
        for morph in self.morphs:
            if morph.base == base:
               return True
        return False

    def check_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
               return True
        return False
    
    def check_pos1(self, pos1):
        for morph in self.morphs:
            if morph.pos1 == pos1:
               return True
        return False

    def get_base_havingpos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
               return morph.base
        return None
      
    def get_base_havingpos1(self, pos1):
        for morph in self.morphs:
            if morph.pos1 == pos1:
               return morph.base
        return None

def make_chunks(cabocha_file):

    srcs_dict = defaultdict(list) # キーは係り先、バリューは係り元のリスト
    morphs    = list()
    one_sentence  = list()
    all_sentences = list()

    for line in cabocha_file: 
        line = line.strip()

        if line.startswith("*"):
           morphs = list()
           items = line.split(" ")
           dst   = int(items[2].replace("D", ""))
           srcs_dict[dst].append(int(items[1]))
           one_sentence.append(Chunk(morphs, dst, srcs_dict[int(items[1])]))

        elif "\t" in line:
           line  = line.replace("\t", ",").replace("、", "").replace("。", "")
           items = line.split(",")
           morphs.append(Morph(items[0], items[7], items[1], items[2]))
        elif "EOS" in line:
           all_sentences.append(one_sentence)
           one_sentence = list()
           srcs_dict = defaultdict(list)

    return all_sentences

def main():
    
    cabocha_file  = open(sys.argv[1], "r")
    all_sentences = make_chunks(cabocha_file)
    cabocha_file.close()

    for one_sentence in all_sentences:
        for chunk in one_sentence:
            phrase  = str()
            for morph in chunk.morphs:
                phrase += morph.surface
            print phrase, chunk.dst, chunk.srcs
    

if __name__ == "__main__":
   main()

