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
  re_tag = re.compile('(<ref>.*|<ref .*)')
  re_accent = re.compile('\'\'+')
  re_blank = re.compile('<br.*?>')
  re_link = re.compile('\[\[(([^\|\]]*?\|)|([^\|\]]*?))([^\|\]]*?)\]\]')
  
  for line in file:
    match = category.search(line)
    if match is not None:
      dict[match.group(1)] = match.group(2)
  
  for i, j in dict.items():
    j = re_tag.sub('', j)
    j = re_accent.sub('', j)
    j = re_link.sub(lambda sub: sub.group(4), j)
    j = re_blank.sub('', j)
    print i,j
  file.close()
