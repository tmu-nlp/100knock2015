#!/usr/bin/python
# _*_ coding:utf-8 _*_

from gensim.models import word2vec
import sys

def main():
    input_file = open(sys.argv[1], "r")
    flag = False    
    for line in input_file:
        line = line.strip()
        if ": family" in line:
           flag = True
           continue
        if flag: 
           if ":" in line:
               break
           print line   
    input_file.close()
    
    

if __name__=="__main__":
   main()
