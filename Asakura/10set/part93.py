#!/usr/bin/python
#coding:utf-8

from gensim.models import word2vec



if __name__ == '__main__':
	model = word2vec.Word2Vec.load('matrix.model')
	input_file = open('part92.txt')
        correct_count = 0
        all_count = 0
	for line in input_file:
	    words = line.strip().split()
            all_count += 1
            if words[3] == words[4]:
                correct_count += 1
        print 'accuracy:%f'%(correct_count/float(all_count))
            
