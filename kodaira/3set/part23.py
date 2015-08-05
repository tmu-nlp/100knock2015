#coding: utf-8
# Jsonファイルの読み込み

if __name__ == "__main__":
  import re
  import sys
  file = open(sys.argv[1], 'r')
  
  # 正規表現
  category = re.compile('(=+)([^=]*)=+')
  for line in file:
    match = category.search(line)
    if match is not None:
      print 'セクション：' + match.group(2) + '\t' + 'レベル:' + str(int(len(match.group(1) ) - 1) )

  file.close()
