#!/usr/bin/python
#coding:utf-8

from gensim.models import word2vec
import pickle
if __name__ == '__main__':
	model = word2vec.Word2Vec.load('matrix.model')
	input_file = open('country_name_list')
        country_list = list()
        matrix_dict = dict()
        for country in input_file:
            country = country.strip()
            country_list.append(country.replace(' ','_'))
        print country_list
	for country in country_list:
            try:
                matrix_dict[country.strip()] = model[country]
                print model[country.strip()]
            except KeyError:
	        pass
        for value in matrix_dict.values():
            print value
        pickle.dump(matrix_dict,open('matrix_dict.dump','w'))
        pickle.dump(country_list,open('country_list.dump','w'))

