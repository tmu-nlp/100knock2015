#coding: utf-8
#テキストの一列目、二列目を抜き出す
#確認コマンド：　cut -f num *.txt  第Nフィールドのものを抜き出す

if __name__ == "__main__":

  import sys

  # open file
  fin = open(sys.argv[1], 'r')
  col1 = open('col1.txt', 'w')
  col2 = open('col2.txt', 'w')

  for line in fin:
    words = line.split('\t')
    col1.write(words[0] + '\n')
    col2.write(words[1] + '\n')
  col1.close()
  col2.close()