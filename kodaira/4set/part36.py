#coding: utf-8

from part30 import *
from collections import defaultdict
from collections import OrderedDict

def getWordFreqDict(mecab_file):
  line_list = makeLineList(mecab_file)
  
  base = 'base'
  word_frequency = defaultdict(lambda:0)

  for morpheme_list in line_list:
    for morpheme_dict in morpheme_list:
      word_frequency[morpheme_dict[base] ] += 1
            
  return word_frequency
  
if __name__ == "__main__":
  import sys
  
  mecab_file = open(sys.argv[1], 'r')
  
  freq_words = getWordFreqDict(mecab_file)
  for i, j in freq_words.items():
    print i, j
    
    
    
    