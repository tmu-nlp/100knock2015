#!usr/bin/python

import random
import math
import pickle
from part73 import *

def make_feature_list(polarity_lines):
    dat = list()
    dat_t = list()
    for line in (polarity_lines):
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
    

def predict_label(polarity_lines, num):
    predict_file = open('predict' + str(num) +'.txt', 'w')
    dat_t, dat = make_feature_list(polarity_lines)
    for correct, feat_list in zip(dat_t, dat):
        predict, prob = logi_reg.predict(feat_list)
        if predict:
            predict_file.write('\t'.join((str(correct), '1', str(prob) ) ) )
        else:
            predict_file.write('\t'.join((str(correct), '0', str(prob) ) ) )
        predict_file.write('\n')
       


if __name__ == "__main__":
    polarity_file = open('polarity.dat', 'r').readlines()
    seg_num = len(polarity_file) / 5
    for num in range(5):
        logi_reg = logistic_regression(0.01)
        logi_reg.weights = pickle.load(open('weight' + str(num) + '.pkl') )
        predict_label(polarity_file[seg_num * num : seg_num * (num + 1)], num )

'''
class logistic_regression:

    
    def predict(self, feat_list):
        prob = self.sigma(feat_list)
        if prob > 0.5:
            return (1, prob)
        else:
            return (0, prob)
'''
