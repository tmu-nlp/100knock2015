#!/usr/bin/python
#coding:utf-8

from gensim.models import word2vec

if __name__ == '__main__':
	model = word2vec.Word2Vec.load('matrix.model')
	input_file = open('combined.csv')
	for line in input_file:
	    words = line.strip().split(',')
            try:
                print line.strip()+' '+str(model.similarity(words[0],words[1]))
            except KeyError:
		pass
