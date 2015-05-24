#coding: utf-8
# Jsonファイルの読み込み

if __name__ == "__main__":
  import re
  import sys
  from collections import OrderedDict
  file = open(sys.argv[1], 'r')
  
  # 正規表現
  dict = OrderedDict()
  
  category = re.compile('\|(.*) = (.*)')
  re_tag = re.compile('<.*?>')
  for line in file:
    match = category.search(line)
    if match is not None:
      dict[match.group(1)] = match.group(2)
  
  import json
  from urllib import urlopen
  wiki_api = 'http://ja.wikipedia.org/w/api.php?action=query&format=json&titles=Image:%s&prop=imageinfo&iiprop=url'

    
  for i, j in dict.items():
    if i == '国旗画像':
      # urlopen でinstance　を呼び、read（）でstrに変換
      json_sentence = urlopen(wiki_api % j).read()
      
      # json 形式なのでjson.loadsで辞書に変換
      dict_sentence = json.loads(json_sentence)
      # 辞書のからurl参照
      url = dict_sentence['query']['pages']['-1']['imageinfo'][0]['url']
      print url
      break
  file.close()