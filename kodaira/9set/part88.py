#!usr/bin/python


import numpy
import pickle



def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )


if __name__ == '__main__':
    matrix_data = numpy.loadtxt('decom_matrix.csv' delimiter = ',') 
    ppmi_dict = pickle.load(open('ppmi.pkl') )
    voc = sorted(ppmi_dict.keys() )
    england_index = voc.index('England')
    gyo, retu = matrix_data.shape
    cos_list = list()
    england_vec = matrix_data[england_index]
    for num in range(gyo):
        cos_list.append(vec_cos(england_vec, matrix[num]) )
    descend_list = sorted(cos_list, reverse = True)
    for score in descend_list[1: 11]:
        print voc[cos_list.index(score)], score

