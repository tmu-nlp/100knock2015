#!/usr/bin/python
#coding: UTF-8
import random

pn_list = []
p_list = []
n_list = []
for line in open("rt-polarity.pos"):
	p_list.append("+1 "+ line.rstrip())
for line in open("rt-polarity.neg"):
	n_list.append("-1 "+ line.rstrip())
pn_list.extend(p_list)
pn_list.extend(n_list)
random.shuffle(pn_list)
senti_file = open("sentiment.txt","w")
for i in pn_list:
	senti_file.write(i + "\n")
