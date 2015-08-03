#!/usr/bin/python
#coding:utf-8

from gensim.models import word2vec



if __name__ == '__main__':
	model = word2vec.Word2Vec.load('matrix.model')
	input_file = open('family.txt')
	for line in input_file:
	    words = line.strip().split()
            try:
                print line.strip()+' '+str(model.most_similar(positive=[words[1],words[2]],negative=[words[0]])[0][0])
            except KeyError:
		pass
