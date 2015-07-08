#!usr/bin/python
import sklearn.decomposition 
import numpy

dim = 300

data = numpy.loadtxt('matrix.csv', delimiter = ',')
pca = sklearn.decomposition.PCA(dim)

result = pca.fit_transform(data)
numpy.savetxt('decom_matrix.csv', result, delimiter = ',')
