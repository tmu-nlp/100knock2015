#coding: utf-8
# Jsonファイルの読み込み

if __name__ == "__main__":
  import re
  import sys
  file = open(sys.argv[1], 'r')
  
  # 正規表現
  category = re.compile('\[\[Category:.*\]\]')
  for line in file:
    if category.search(line) is not None:
      print line,

  file.close()
