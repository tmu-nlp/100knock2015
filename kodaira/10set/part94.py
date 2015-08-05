#!usr/bin/python


import numpy
import pickle


def vec_cos(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y) )


def get_vec(word):
    return matrix_data[voc.index(word)]


def cul_similar(a, b):
    return str( vec_cos(get_vec(a), get_vec(b) ) )

    
def culc_all(fname):
    for line in open (fname):
        a, b, c = line.split('\t')
       
        try:
            print (line.strip() + '\t' + cul_similar(a, b) )
        except KeyboardInterrupt:
            print 'key interrupt'
            exit()
        except:
            print (line.strip() + '\t' + str(0) )


def load_vec(csv_file):
    matrix_data = numpy.genfromtxt(csv_file, delimiter = ',')
    matrix_data[numpy.isnan(matrix_data)] = 0
    return matrix_data

if __name__ == '__main__':
    matrix_data = load_vec('vector.csv')
    voc = open('word.txt').read().split('\n')
    culc_all("analogy/combined.tab")
