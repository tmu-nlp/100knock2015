#coding: utf-8

from part30 import *
        
if __name__ == "__main__":
  import sys
  mecab_file = open(sys.argv[1], 'r')
  
  sahen_noun = 'サ変接続'; pos1 = 'pos1'; surface = 'surface'
 
  line_list = makeLineList(mecab_file)
  for morpheme_list in line_list:
    for morpheme_dict in morpheme_list:
      if morpheme_dict[pos1] == sahen_noun:
        
        print morpheme_dict[surface],
    
