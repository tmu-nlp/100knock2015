#coding: utf-8

from part30 import *

def joinNoun(word1, word2):
   if word2.islower():
     return word1 + ' ' + word2
   else:
     return word1 + word2

if __name__ == "__main__":
  import sys
  mecab_file = open(sys.argv[1], 'r')
  
  Noun = '名詞'; pos = 'pos'; surface = 'surface'
  max_count = 0
  longest_noun = list()
  line_list = makeLineList(mecab_file)
  
  for morpheme_list in line_list:
    count = 0
    noun = ''
    for num in range(0, len(morpheme_list) - 1 ):
    
      if morpheme_list[num][pos] == Noun and num != len(morpheme_list) - 1:
        count += 1
        noun = joinNoun(noun, morpheme_list[num][surface])
        
      else:
        if count >= max_count and noun != '':
          if count == max_count:
            longest_noun.append(noun)
          else:
            longest_noun = list()
            longest_noun.append(noun)
            max_count = count
        noun = ''
        count = 0
      #end for num---
  #end for mor----
           
  for no in longest_noun:
    print no