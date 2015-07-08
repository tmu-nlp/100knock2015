#!usr/bin/python


import numpy
import pickle


matrix_data = numpy.loadtxt('decom_matrix.csv' delimiter = ',') 
ppmi_dict = pickle.load(open('ppmi.pkl') )
voc = sorted(ppmi_dict.keys() )
index = voc.index('United_State')
print matrix_data[index]
