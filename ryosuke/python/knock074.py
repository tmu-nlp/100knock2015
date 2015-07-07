# coding:utf-8
"""
python knock074.py ../Data/result/knock073/python/model073.txt
"""

import sys
import math
from stemming.porter2 import stem
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

model = dict()
read_model(model)
for line in iter(sys.stdin.readline, '\n'):
    feat = extract_features(line.strip())
    print predict(probability(feat), 0.5)
