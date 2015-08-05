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


def make_morph(cabocha_file):

    all_sentences = list()
    one_sentence  = list()

    for line in cabocha_file:
        line = line.strip()

        if line.startswith("*"):
           continue

        if "\t" in line:
           line  = line.replace("\t", ",")
           items = line.split(",") 
           one_sentence.append(Morph(items[0], items[7], \
                                     items[1], items[2]))
        if "EOS" in line:
            all_sentences.append(one_sentence)
            one_sentence = list()
    return all_sentences

def main():
    
    cabocha_file  = open(sys.argv[1], "r")
    all_sentences = make_morph(cabocha_file)
    cabocha_file.close()

    for one_sentence in all_sentences:
        for morph in one_sentence:
            print morph.surface, morph.base, morph.pos, morph.pos1



if __name__=="__main__":
   main()
