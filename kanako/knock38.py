#!usr/bin/python
#coding:utf-8
from knock36 import word_freq
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

top10_graph = {}
hist_freq = []
count = 0
for word, freq in sorted(word_freq().items(), key = lambda x:-x[1]):
	hist_freq.append(int(freq))

plt.rc('font', **{'family': 'serif'})
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(hist_freq,bins=100,range=(0,100),normed=False)
ax.set_xlabel('Word')
ax.set_ylabel('Frequency')
plt.show()

