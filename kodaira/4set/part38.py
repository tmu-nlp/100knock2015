#coding: utf-8
# 参考：http://akiyoko.hatenablog.jp/entry/2013/06/07/213448

from part36 import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as mlab

def printHistgram(word_freq_dict):
  # 初期設定（フォント:familyはフォント名 serifはひげなし)
  plt.rc('font', **{'family': 'serif'})
  # キャンバス
  fig = plt.figure()
  ax = fig.add_subplot(111)
  # 値のリスト, 分割数, 表示範囲
  ax.hist(word_freq_dict.values(), bins = 10, range = (0, 50) )
  # グリッド線の描画
  ax.grid(True)
  # title
  ax.set_title('Word Frequency Histgram', size = 16)
  ax.set_xlabel('Frequency', size = 14)
  ax.set_ylabel('Kind', size = 14)
  # 表示
  plt.show()
  
if __name__ == '__main__':
  import sys

  mecab_file = open(sys.argv[1], 'r')
  word_freq_dict = getWordFreqDict(mecab_file)
  printHistgram(word_freq_dict)
