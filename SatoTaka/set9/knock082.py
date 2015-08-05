#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import random

def main():
    
    input_file = open(sys.argv[1], "r")

    for line in input_file:
        words = line.strip().split(" ")
        for index in range(len(words)):
            word_list = list()
            word_list.append(words[index])
#            if acceptable_forward >= 0 and acceptable_backward <= len(words)-1:
#               for i in range(acceptable_forward, acceptable_backward + 1):
#                   word_list.append(words[i])
#               print "\t".join(word_list)
#               continue
            d = random.randint(1,5) 
            for i in range(index-1, index-d-1, -1):
                if i >= 0:
                   word_list.append(words[i])
                else:
                   break
            for i in range(index+1, index+d+1):
                if i <= len(words) -1:
                   word_list.append(words[i])
                else:
                   break
            print "\t".join(word_list)

    input_file.close()
    

if __name__=="__main__":
   main()
