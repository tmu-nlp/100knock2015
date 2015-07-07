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
    pre = tp/(tp+fp) if tp+fp != 0 else 0
    rec = tp/(tp+fn) if tp+fn != 0 else 0
    return pre, rec

model = dict()
read_model(model)
probs = list()
golds = list()
pres = list()
recs = list()

# create prob list
count = .0
all_count = len(open(sys.argv[2]).readlines())
for line in open(sys.argv[2]):
    spl = line.strip().split() 
    gold = spl[0]
    feat = extract_features(spl[1:])
    prob = probability(feat)
    probs.append(prob)
    golds.append(gold)
    count += 1
    print '\r %d%%' % (100*count/all_count),

split_num = 20
for thresh in (1.0*i/split_num for i in range(0, split_num, 1)):
    tp = .0
    fp = .0
    tn = .0
    fn = .0
    for prob, gold in zip(probs, golds):
        pred = predict(prob, thresh)
        if gold != pred and pred == '+1':
            fp += 1
        elif gold != pred:
            fn += 1
        elif gold == pred and pred == '+1':
            tp += 1
        elif gold == pred:
            tn += 1
        else:
            print "error"
            exit()
        
    pre, rec = calc_pre_rec(tp, fp, tn, fn)
    pres.append(pre)
    recs.append(rec)

plt.plot(recs, pres, 'o')
plt.axis([0,1,0,1])
plt.xlabel('recall')
plt.ylabel('precision')
plt.show()
