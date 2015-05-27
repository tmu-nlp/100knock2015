#coding: utf-8


import json
# 一文ごとに形態素のリストを作ってリストに格納
def makeLineList(mecab_file):
   # 形態素ごとの解析結果の辞書を格納
  morpheme_list = list()
  # 一文ごとの形態素の辞書のリストを格納
  line_list = list()
  # 表層系             基本形           品詞        品詞細分類
  surface = 'surface'; base = 'base'; pos = 'pos'; pos1 = 'pos1'
  
  #　形態素ごとの読み取り
  for line in mecab_file:
    morpheme_dict = {}
    line = line.strip()
    line = line.split('\t')
    # if line is end of a sentence, skip or add list
    if line[0] == 'EOS':
      # if morpheme_list has morpheme_dict , add morpheme_list to line_list and initialize the morpheme_list
      if len(morpheme_list) != 0:
        line_list.append(morpheme_list)
        morpheme_list = list()
      continue
    else:
      morpheme_dict[surface] = line[0]
    result = line[1].split(',') 
    
    morpheme_dict[base] = result[6]
    morpheme_dict[pos] = result[0]
    morpheme_dict[pos1] = result[1]
    
    # append dict to list
    morpheme_list.append(morpheme_dict)
 
  return line_list
  
# 文字化けしないでプリントできるやつ
def pp(obj):
  if isinstance(obj, list) or isinstance(obj, dict):
    orig = json.dumps(obj, indent=4)
    print eval("u'''%s'''" % orig).encode('utf-8')
  else:
    print obj
  
    
        
if __name__ == "__main__":
  import sys
  mecab_file = open(sys.argv[1], 'r')
 
  line_list = makeLineList(mecab_file)
  pp(line_list)
    