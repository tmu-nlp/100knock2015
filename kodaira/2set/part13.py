#coding: utf-8
#col1 col2を水平にタブ区切りでくっつける
#確認コマンド：　paste file1 file2

if __name__ == "__main__":
  import sys

  # open file
  col1 = open('col1.txt', 'r')
  col2 = open('col2.txt', 'r')

  for (c1, c2) in zip(col1, col2):
    print c1.strip() + '\t' + c2,