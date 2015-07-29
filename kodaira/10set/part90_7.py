#!usr/bin/python


import numpy
import pickle



def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )
if __name__ == '__main__':
    matrix_data = numpy.genfromtxt('vector.csv', delimiter = ',') 
    voc = open('word.txt').read().split('\n')
    index = voc.index('United_States')
    index_ = voc.index('U.S')

    x = matrix_data[index][:-1]
    y = matrix_data[index_][:-1]

    print vec_cos(x, y)
