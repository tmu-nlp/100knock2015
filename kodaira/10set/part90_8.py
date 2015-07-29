#!usr/bin/python


import numpy
import pickle



def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )


if __name__ == '__main__':
    matrix_data = numpy.genfromtxt('vector.csv', delimiter = ',') 
    voc = open('word.txt').read().split('\n')

    england_index = voc.index('England')
    gyo, retu = matrix_data.shape
    cos_list = list()
    england_vec = matrix_data[england_index]
    for num in range(gyo):
        cos_list.append(vec_cos(england_vec[:-1], matrix[num][:-1]) )
    descend_list = sorted(cos_list, reverse = True)
    for score in descend_list[1: 11]:
        print voc[cos_list.index(score)], score

