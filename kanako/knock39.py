#!usr/bin/python
#coding:utf-8
from knock36 import word_freq
import matplotlib.pyplot as plt

top10_graph = {}
plot_freq = []
count = 0
for word, freq in sorted(word_freq().items(), key = lambda x:-x[1]):
	plot_freq.append(int(freq))
X = range(1,len(plot_freq)+1)
Y = plot_freq
plt.plot(X,Y,'o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Ranking')
plt.ylabel('Frequency')
plt.show()

