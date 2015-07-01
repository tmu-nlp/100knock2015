#!/usr/bin/python
# _*_ coding:utf-8 _*_

import math

def main():
    model_file = open("model_73.txt")
    input_file = open("sentiment_without_label.txt")

    word_weight = dict()
    exponent    = float()
    probablity  = float()
    
    for line in model_file:
        if line.startswith("@") and "bias" in line:
           bias = line.strip().split("\t")[1]
        elif "@" not in line:
           weight, word = line.strip().split("\t")
           word_weight[word] = float(weight)

    for line in input_file:
        words = line.strip().split(" ")
        score = 0
        for word in words:
            if word in word_weight:
               score += word_weight[word]
#        if score >= 0:
#           print "+1 "+ line.strip(),
#        else:
#           print "-1 "+ line.strip(),
        exponent = math.exp(-(score + int(bias)))
        probablity = 1/(1+exponent)
#        print probablity
        if probablity >= 0.5:
           print "+1 "+line.strip()+ str(probablity)
        else:
           print "-1 "+line.strip()+ str(probablity)
        exponent   = float()
        probablity = float()

    model_file.close()
    input_file.close()



if __name__=="__main__":
   main()
