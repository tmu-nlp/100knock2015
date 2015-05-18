#coding: utf-8
#テキストの先頭から指定列を抜き取る
#確認コマンド：head -n N *.txt

if __name__ == "__main__":

  import sys
        
  # open file
  fin = open(sys.argv[1], 'r')
  
  # set num
  num = int(sys.argv[2])
  
  # 行ごとに格納
  lines = fin.readlines()
  
  #print
  print lines[num - 1],