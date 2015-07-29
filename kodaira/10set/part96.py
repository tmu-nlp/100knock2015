#!usr/bin/python


import numpy
import pickle


def get_vec(word):
    return matrix_data[voc.index(word)]


def get_country_vec(fname, voc, matrix_data):
    country_name_list = list()
    country_vec_list = list()
    for line in open (fname):
        try:
            country_vec_list.append(get_vec(line.strip() ) )
            country_name_list.append(line.strip() )
        except KeyboardInterrupt:
            print 'key interrupt'
            exit()
        except:
            continue
    print country_name_list
    return country_name_list, country_vec_list

def load_vec(csv_file):
    matrix_data = numpy.genfromtxt(csv_file, delimiter = ',')
    matrix_data[numpy.isnan(matrix_data)] = 0
    return matrix_data

if __name__ == '__main__':
    matrix_data = load_vec('vector.csv')
    voc = open('word.txt').read().split('\n')

    a, b = get_country_vec("countrys.txt", voc, matrix_data)

    pickle.dump(list((a, b)), open('country_data.pkl', 'w') )

