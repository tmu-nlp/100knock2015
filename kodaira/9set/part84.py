#!usr/bin/python

import pickle
import math
import numpy
from collections import defaultdict
ppmi_dict = defaultdict(lambda:defaultdict(float) ) 
cont_dict = pickle.load(open('cont.pkl') )
co_occur_dict = pickle.load(open('co_occur.pkl') )
word_dict = pickle.load(open('word.pkl') )

voc_set = set()
count = 142425660
print 'start store ppmi'
for pair, freq in co_occur_dict.items():
    if freq > 9:
        word, cont = pair.split('\t')
        numer = count * freq; denom = word_dict[word] * cont_dict[cont]
        if numer > denom:
            voc_set.update(cont)
            #ppmi_dict[pair] = math.log(numer / denom)
            ppmi_dict[word][cont] = math.log(numer / float(denom) )
voc_set.update(word_dict.keys() )


print 'start convert to matrix'
vocablary = sorted(ppmi_dict.keys())
all_voc = sorted(list(voc_set) )
term_document_matrix = numpy.zeros((len(all_voc), len(vocablary)) )

print 'make_zeros_matrix'
x_count = 0;
for x_voc in vocablary:
    temp_matrix = term_document_matrix[x_count]
    y_count = 0
    x_count += 1
    for y_voc in all_voc:
        if x_voc in ppmi_dict and y_voc in ppmi_dict[x_voc]:
             temp_matrix[y_count] = (ppmi_dict[x_voc][y_voc])
             y_count += 1
print 'write csv'
numpy.savetxt('matrix.csv', term_document_matrix, delimiter = ',')

#pickle.dump(ppmi_dict, open('ppmi.pkl', 'w') )
#pickle.dump(term_document_matrix, open('matrix.pkl', 'w') )

