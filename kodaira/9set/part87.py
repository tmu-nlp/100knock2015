#!usr/bin/python


import numpy
import pickle



def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )
if __name__ == '__main__':
    matrix_data = numpy.loadtxt('decom_matrix.csv' delimiter = ',') 
    ppmi_dict = pickle.load(open('ppmi.pkl') )
    voc = sorted(ppmi_dict.keys() )
    index = voc.index('United_State')
    index_ = voc.index('U.S')

    x = matrix_data[index]
    y = matrix_data[index_]

    print vec_cos(x, y)
