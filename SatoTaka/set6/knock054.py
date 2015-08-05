#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

def Tagging(stanford_file):

  r = re.compile("<word>(.+?)<|<lemma>(.+?)<|<POS>(.+?)<")

  for line in stanford_file:
      if r.search(line):
         if "word" in line:
           print r.search(line).group(1) +"\t", 
         elif "lemma" in line:
           print r.search(line).group(2) +"\t",
         elif "POS" in line:
           print r.search(line).group(3)

def main():

  stanford_file = open("nlp.txt.xml")
  Tagging(stanford_file)
  stanford_file.close()

if __name__=="__main__":
  main()
