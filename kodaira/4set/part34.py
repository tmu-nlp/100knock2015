#coding: utf-8

from part30 import *
        
if __name__ == "__main__":
  import sys
  mecab_file = open(sys.argv[1], 'r')
  
  Noun = '名詞'; pos = 'pos'; surface = 'surface'
 
  line_list = makeLineList(mecab_file)
  for morpheme_list in line_list:
    for num in range(1, len(morpheme_list) - 1 ):
      if morpheme_list[num][surface] == 'の':
        if morpheme_list[num - 1][pos] == Noun and morpheme_list[num + 1][pos] == Noun:
          print morpheme_list[num - 1][surface] + morpheme_list[num][surface] + morpheme_list[num + 1][surface]
