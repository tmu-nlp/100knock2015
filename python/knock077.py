# coding:utf-8
"""
python knock077.py ../Data/result/knock076/python/labeling.txt
"""

import sys

tp = .0
fp = .0
tn = .0
fn = .0

for line in open(sys.argv[1]):
    gold, pred,_ = line.strip().split()
    
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

acc = (tp+tn)/(tp+tn+fn+fp)
pre = tp/(tp+fp)
rec = tp/(tp+fn)
f = (2*rec*pre)/(rec+pre)
print 'Accuracy %f, precision %f, recall %f, F1 %f' % (acc, pre, rec, f)
