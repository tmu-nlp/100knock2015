#!usr/bin/python
#coding:utf-8
from knock36 import word_freq
import matplotlib.pyplot as plt

top10_graph = {}
top10_key = []; top10_value = []
count = 0
for word, freq in sorted(word_freq().items(), key = lambda x:-x[1]):
	top10_key.append(word.decode('utf-8'))
	top10_value.append(int(freq))
	count += 1
	if count == 10:
		break
for i in top10_value:
	print i
X = range(1,11)
Y = top10_value
plt.bar(X,Y) 
plt.xticks(X, top10_key)
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.show()

