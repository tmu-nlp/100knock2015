#!/usr/bin/python
# _*_ coding:utf-8 _*_

def Tokenization(stanford_file):
  for line in stanford_file:
    if "<word>" in line:
       print line.strip().replace("\t", "").replace("<word>","").replace("</word>", "")
    

def main():

  stanford_file = open("nlp.txt.xml")
  Tokenization(stanford_file)
  stanford_file.close()

if __name__ == "__main__":
  main()
