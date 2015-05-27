#coding: utf-8
# 参考：http://ss9neco.blog.fc2.com/blog-entry-36.html


from part36 import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as np

def logLogGraph(word_freq_dict):
  freq_list = list()
  for i, j in sorted(word_freq_dict.items(), key = lambda x: -x[1]):
    freq_list.append(j)
  
  plt.semilogy(freq_list)
  plt.semilogx(range(0, len(freq_list)))
  plt.title('Log-log graph')
  plt.xlabel('Rank')
  plt.ylabel('Frequency')
  plt.show()
if __name__ == '__main__':
  import sys

  mecab_file = open(sys.argv[1], 'r')
  word_freq_dict = getWordFreqDict(mecab_file)
  logLogGraph(word_freq_dict)