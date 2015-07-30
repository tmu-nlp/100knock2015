#!/usr/bin/python
# _*_ coding:utf-8 _*_

def PERSON_extract(stanford_file):
  item_name = str()
  for line in stanford_file:
      line = line.strip().replace("\t", "")
      if "<word>" in line: 
         item_name = line.replace("<word>","").replace("</word>", "")

      if "PERSON" in line:
         print item_name
         item_name = str()

def main():

  stanford_file = open("nlp.txt.xml")
  PERSON_extract(stanford_file)
  stanford_file.close()

if __name__=="__main__":
  main()
