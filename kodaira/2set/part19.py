#coding: utf-8
#一行目の文字列の出現頻度を求め、出現頻度の高い順に並べる。


if __name__ == "__main__":
  import sys

  file = open(sys.argv[1], 'r')
  dict = {}
  for line in file:
    line = line.split('\t')
    if line[0] in dict:
      dict[line[0] ] += 1
    else:
      dict[line[0] ] = 1

  for word, num in sorted(dict.items(), key = lambda x: x[1] , reverse = True):
    print word, num
