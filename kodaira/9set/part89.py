#!usr/bin/python


import numpy
import pickle



def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )
def get_vec(word):
    return matrix_data[voc.index(word)]

if __name__ == '__main__':
    matrix_data = numpy.loadtxt('decom_matrix.csv' delimiter = ',') 
    ppmi_dict = pickle.load(open('ppmi.pkl') )
    voc = sorted(ppmi_dict.keys() )
    vector = get_vec('Spain') - get_vec('Madrid') + get_vec('Athens')
    gyo, retu = matrix_data.shape
    cos_list = list()
    for num in range(gyo):
        cos_list.append(vec_cos(vector, matrix[num]) )
    descend_list = sorted(cos_list, reverse = True)
    for score in descend_list[0: 10]:
        print voc[cos_list.index(score)], score

