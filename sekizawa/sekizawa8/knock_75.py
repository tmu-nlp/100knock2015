#!usr/bin/python
#coding:utf-8

from collections import defaultdict

if __name__ == "__main__":
    model_file = open("knock_73.model", "r")
    weight_dict = defaultdict(lambda: 0)
    score = 0.0
    count = 0

    for line in model_file:
        if "@" not in line:
            print line
            weight, stem = line.strip().split("\t")
            if type(weight) != float:
                if stem != "__BIAS__":
                    weight_dict[stem] = float(weight)

    for stem, weight in sorted(weight_dict.items(), key = lambda x:x[1], reverse = True):
        if count < 10:
            print stem + "\t" + str(weight)
            count += 1
        else:
           count = 0
           break
    for stem, weight in sorted(weight_dict.items(), key = lambda x:x[1]):
        if count < 10:
            print stem + "\t" + str(weight)
            count += 1
        else:
            break

