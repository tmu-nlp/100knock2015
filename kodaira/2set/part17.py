#coding: utf-8
#一列目の名前の集合を求める
#確認コマンド: ソートしたファイルに    uniq *.txt
if __name__ == "__main__":

  import sys

  # open file
  file = open(sys.argv[1])

  # make set
  set = set()

  # add
  for line in file:
    line = line.strip()
    words = line.split('\t')
    set.add(words[0])
  
  # print
  for word in set:
    print word