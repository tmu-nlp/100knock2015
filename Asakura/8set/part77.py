#usr/bin/python
#coding:utf-8

import math
from collections import defaultdict

def main():
    predict_list = list()
    label_list = list()
    model_dict = defaultdict(lambda:0)
    model_file = open('part73.model')
    for num,line in enumerate(model_file):
        if num < 2:
            continue
        value, key = line.strip().split()
        model_dict[key] = float(value)


    for line in open('sentiment.txt'):
        sum_weight = model_dict['__BIAS__']
        word_list = line.strip().split()
        label = line.strip().split()[0]
        sentence = ' '.join(word_list[1:])
        for word in word_list[1:]:
#            print model_dict[word]
#            print word
            sum_weight -= float(model_dict[word])
        p = 1 / (1 + float(math.exp(sum_weight)))
        if p > .5:
            predict_label = '+1'
        else:
            predict_label = '-1'
        predict_list.append(predict_label)
        label_list.append(label)
    match = 0
    for predict,label in zip(predict_list,label_list):
        if predict == label:
            match += 1

    precision = float(match)/len(predict_list)#precisionとrecallが同じ値になる...
    recall = float(match)/len(label_list)
    F = 2*precision*recall/(precision+recall)
    print 'precision:%f\trecall:%f\tF値:%f'%(precision,recall,F)
if __name__ == '__main__':
    main()
