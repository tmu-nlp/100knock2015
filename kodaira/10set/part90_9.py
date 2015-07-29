#!usr/bin/python


import numpy
import pickle



def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )
def get_vec(word):
    return matrix_data[voc.index(word)]

if __name__ == '__main__':
    matrix_data = numpy.genfromtxt('vector.csv', delimiter = ',')
    matrix_data[numpy.isnan(matrix_data)] = 0
    voc = open('word.txt').read().split('\n')
    vector = get_vec('Spain') - get_vec('Madrid') + get_vec('Athens')
    gyo, retu = matrix_data.shape
    cos_list = list()
    for num in range(gyo):
        cos_list.append(vec_cos(vector, matrix_data[num]) )
    descend_list = sorted(cos_list, reverse = True)
    for score in descend_list[0: 10]:
        print voc[cos_list.index(score)], score

