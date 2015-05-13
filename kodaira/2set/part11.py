#coding: utf-8
#タブをスペースに変換
#確認コマンド： expand -t 1 *.txt

if __name__ == "__main__":
  
  import sys
  
  # open file
  fin = open(sys.argv[1], 'r')\

  # replace
  for line in fin:
    line = line.replace('\t', ' ')
    print line,