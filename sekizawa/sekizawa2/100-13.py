#!/usr/bin/python
#coding: utf-8

if __name__ == "__main__":

    f1 = open("col1.txt", "r")
    f2 = open("col2.txt", "r")
    f3 = open("col3.txt", "w")

    for line1 in f1:
        for line2 in f2:
            f3.write(line1.rstrip()),
            f3.write("\t"),
            f3.write(line2.rstrip()),
            f3.write("\n"),
            break

    f1.close()
    f2.close()
    f3.close()
 
