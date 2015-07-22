#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

import sys

def delete_symbol_first(word):
    if not word:
       return word
    if word[0] not in removelist:
       return word
    else:
       word = word[1:]
       return delete_symbol_first(word)
    
def delete_symbol_last(word):

    if word[-1] not in removelist:
       return word
    else:
       word = word[:len(word)-1]
       return delete_symbol_last(word)


def main():
    input_file = open(sys.argv[1], "r")
    for line in input_file:
        words = line.strip().split(" ")
        if not words[0]:
          continue
        for word in words:
            word = delete_symbol_first(word)
            if word == "":
               continue
            word = delete_symbol_last(word)
            if word == "":
               continue
            print word,
        print 

    input_file.close()

if __name__=="__main__":

   removelist = [".", ",", "!", "?", ":", ";", "(", ")", "[", "]", "'", '"']
   main()
