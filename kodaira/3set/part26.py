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
  re_accent = re.compile('\'\'+')
  for line in file:
    match = category.search(line)
    if match is not None:
      dict[match.group(1)] = match.group(2)
  
  for i, j in dict.items():
    print re_accent.sub('', j)
  
  file.close()
