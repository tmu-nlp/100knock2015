#coding: utf-8
#行数のカウント
#確認コマンド：wc *.txt

if __name__ == "__main__":
    
  import sys
    
  # open file
  file = open(sys.argv[1], 'r')
  
  # count lines
  lines = file.readlines()
  
  # print
  print len(lines)
