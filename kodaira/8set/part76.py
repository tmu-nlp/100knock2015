#!usr/bin/python

import random
import math
import pickle
from part73 import *

def make_feature_list(polarity_file):
    dat = list()
    dat_t = list()
    for line in open(polarity_file):
        line = line.strip().split()
        if line[0] == '-1':
            dat_t.append(0)
        else:
            dat_t.append(1)
        feat_list = list()
        for feat in line[1:]:
            name, value = feat.split(':')
            feat_list.append((name, value) )
        dat.append(feat_list)
    return dat_t, dat
    

def predict_label(polarity_file):
    dat_t, dat = make_feature_list(polarity_file)
    #print len(logi_reg.weights)
    for correct, feat_list in zip(dat_t, dat):
        predict, prob = logi_reg.predict(feat_list)
        if predict:
            print '\t'.join((str(correct), '1', str(prob) ) )
        else:
            print '\t'.join((str(correct), '0', str(prob) ) )
       


if __name__ == "__main__":
    polarity_file = 'polarity.dat'
    logi_reg = logistic_regression(0.01)
    logi_reg.weights = pickle.load(open('weight.pkl') )
    predict_label(polarity_file)

'''
class logistic_regression:

    
    def predict(self, feat_list):
        prob = self.sigma(feat_list)
        if prob > 0.5:
            return (1, prob)
        else:
            return (0, prob)
'''
