#coding: utf-8


from part36 import *
from collections import OrderedDict

import matplotlib.pyplot as plt

def plotBarChart(top10_words):
  X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  Y =  top10_words.values()
  plt.bar(X, Y, align = 'center')
  key = list()
  for i, j in top10_words.items():
    key.append(i.decode('utf-8'))
  plt.xticks(X, key )
  plt.title('Word Frequency Top 10')
  plt.ylabel('Frequency')
  plt.show()

def makeTop10Word(mecab_file):
  freq_words = getWordFreqDict(mecab_file)
  
  count = 1
  top_words = OrderedDict()
  for word, frequency in sorted(freq_words.items(), key = lambda x:-x[1]):
    top_words[word] = frequency
    count += 1
    if count > 10: break
  return top_words

if __name__ == '__main__':
  import sys

  mecab_file = open(sys.argv[1], 'r')
  top_words = makeTop10Word(mecab_file)
  plotBarChart(top_words)