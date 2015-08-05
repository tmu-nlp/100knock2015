#!/usr/bin/python
#coding: utf-8
from stemming.porter2 import stem
from knock71 import stop_tf

def features_extract():
	train_data = []
	sent_cleaned = []
	stemmed_line = []
	for line in open("sentiment.txt"):
		sent = line.strip().split()[1:]
		label = line.strip().split()[0]
		for word in sent:
			if not stop_tf(word):
				stemmed_word = stem(word)
				sent_cleaned.append(stemmed_word)
		line_cleaned = "%s %s" %(label, " ".join(sent_cleaned))
		train_data.append(line_cleaned)
		sent_cleaned=[]
		line_cleaned=[]
	return train_data

if __name__=='__main__':
	feature_file = open("feature.txt","w")
	train_data = features_extract()
	for line in train_data:
		feature_file.write(line + "\n")
