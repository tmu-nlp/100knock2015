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
  re_ref = re.compile('(.*)(<ref>.*|<ref .*)')
  re_impact = re.compile('\'\'+')
  re_link = re.compile('\[\[(([^\|\]]*?\|)|([^\|\]]*?))([^\|\]]*?)\]\]')
  re_lang = re.compile('\{\{lang\|.*?\|(.*?)\}\}')
  re_file = re.compile('\[\[(File|ファイル)\:(.+?)\|.+\]\]')
  re_br = re.compile('<(br|br )/>')
  for line in file:
    match = category.search(line)
    if match is not None:
      dict[match.group(1)] = match.group(2)
  
  for i, j in dict.items():
    print i,
    j = re_impact.sub('', j)
    j = re_ref.sub(lambda a:a.group(1), j)
    j = re_link.sub(lambda a:a.group(4), j)
    j = re_lang.sub(lambda a:a.group(1), j)
    j = re_file.sub(lambda a:a.group(2), j)
    j = re_br.sub(' ', j)
    print j
  file.close()
