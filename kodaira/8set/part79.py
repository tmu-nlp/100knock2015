#coding: utf-8


import matplotlib.pyplot as plt
import matplotlib.pyplot as np

def draw_graph(result):
  acc_list = list() ; rec_list = list()
  for acc, rec in result):
    acc_list.append(acc); rec_list.append(rec)
  
  #plt.semilogy(freq_list)
  #plt.semilogx(range(0, len(freq_list)))
  plt.plot(acc_list, rec_list)
  plt.title('accuracy - recall')
  plt.xlabel('accuracy')
  plt.ylabel('recall')
  plt.show()
  
if __name__ == '__main__':
  import sys

  result = open(sys.argv[1], 'r')
  draw_graph(result)
