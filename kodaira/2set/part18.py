#coding: utf-8
#第３コラムの数値の降順にそーと
#確認コマンド：sort *.txt

if __name__ == "__main__":
  import sys
  
  # open file
  fin = open(sys.argv[1], 'r')

  # 行ごとに格納
  lines = fin.readlines()

  lines_list = list()

  for line in lines:
    lines_list.append(line.split('\t') )

  lines_list.sort( cmp = lambda x , y: cmp(x[2], y[2]) )

  for line in lines_list:
    print '\t'.join(line),