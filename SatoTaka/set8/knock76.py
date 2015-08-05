#!/usr/bin/python
# _*_ coding:utf-8 _*_

def main():
    labels = open("output_76_raw.txt")
    for line in labels:
        line = line.strip().replace(" ", "\t").replace(":", "\t")
        if not "/" in line:
           print line
    labels.close()

if __name__=="__main__":
   main()
