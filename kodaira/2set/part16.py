#coding: utf-8
#ファイルをN分割
#確認コマンド：split

if __name__ == "__main__":
  import sys
  
  list = list()
  
  # open file
  fin = open(sys.argv[1], 'r')
            
  # set num
  num = int(sys.argv[2])
  
  # 行ごとに格納
  lines = fin.readlines()

  #一ブロックの行数
  gyosu = len(lines) / num
  
  #割ったときのあまり行数
  amari = len(lines) % num
  
  # どこで改行するかの行数のリストを作成
  n = 0
  for i in range (0 , num):
    n += gyosu
    if i >= num - amari:
      n += 1
    list.append(n)
  print list
  # 行数カウント
  count = 0
  
  # listにある行で改行
  for line in lines:
    print line,
    count += 1
    if count in list:
      print ''