# coding:utf-8
"""
python knock079.py ../Data/result/knock073/python/model073.txt ../Data/sentiment.txt
"""

import sys
import math
from stemming.porter2 import stem
import matplotlib.pyplot as plt
from knock071 import is_stop


def read_model(d):
    for line in open(sys.argv[1]):
        if line.startswith('@'):
            continue
        spl = line.strip().split()
        d[spl[1]] = float(spl[0])


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def extract_features(text):
    return [stem(tok) for tok in text if not is_stop(tok)] + ['__BIAS__']


def probability(feat):
    return sigmoid(sum(model.get(f, 0) for f in feat))


def predict(prob, thresh):
    return '-1' if prob < thresh else '+1'

def calc_pre_rec(tp, fp, tn, fn):
    return (tp/(tp+fp)), (tp/(tp+fn))

model = dict()
read_model(model)
x = list()
y = list()
for thresh in (i/100 for i in range(0, 100, 1)):
    tp = .0
    fp = .0
    tn = .0
    fn = .0
    for line in open(sys.argv[2]):
        spl = line.strip().split() 
        gold = spl[0]
        feat = extract_features(spl[1:])
        prob = probability(feat)
        pred = predict(prob, thresh)

        if gold != pred and pred == '+1':
            fp += 1
        elif gold != pred:
            fn += 1
        elif gold == pred and pred == '+1':
            tp += 1
        elif gold == pred:
            tp += 1
        else:
            print "error"
            exit()
        
    pre, rec = calc_pre_rec(tp, fp, tn, fn)
    x.append(pre)
    y.append(rec)

plt.plot(x, y, 'o')
plt.show()
