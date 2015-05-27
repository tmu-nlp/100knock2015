#coding: utf-8

from part30 import *
        
if __name__ == "__main__":
  import sys
  mecab_file = open(sys.argv[1], 'r')
  
  verb = '動詞'; pos = 'pos'; surface = 'surface'
 
  line_list = makeLineList(mecab_file)
  for morpheme_list in line_list:
    for morpheme_dict in morpheme_list:
      if morpheme_dict[pos] == verb:
        print morpheme_dict[surface],
    print ''