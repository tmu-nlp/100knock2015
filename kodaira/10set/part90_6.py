#!usr/bin/python
#refarence:http://qiita.com/okappy/items/e16639178ba85edfee72

import numpy
import pickle


matrix_data = numpy.genfromtxt('vector.csv', delimiter = ',')
word_list = open('word.txt').read().split('\n')
index = word_list.index('United_States')
print matrix_data[index]
