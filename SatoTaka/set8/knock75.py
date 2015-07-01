#!/usr/bin/python
# _*_ coding:utf-8 _*_

from collections import defaultdict 

def main():
    model_file  = open("model73_file.txt")
    word_weight = defaultdict(int)
    for line in model_file:
        if not line.startswith("@"): 
           weight, word = line.strip().split("\t")
           word_weight[word] = float(weight)
    
    count = 0
    for word, weight in sorted(word_weight.items(), key = lambda x:-x[1]):
        print word + "\t" + str(weight)
        count += 1
        if count == 9:
           break

    count = 0
    print 
    for word, weight in sorted(word_weight.items(), key = lambda x:x[1]):
        print word + "\t" + str(weight)
        count += 1
        if count == 9:
           break


    model_file.close()

if __name__=="__main__":
   main()
