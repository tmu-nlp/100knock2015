#!usr/bin/python
#coding:utf-8

import CaboCha

if __name__ == "__main__":

    f = open("neko.txt", "r")
    new = open("neko.txt.cabocha", "w")
    tag = CaboCha.Parser("")

    for line in f:
        line = line.strip()
        if line != "":
            tree = tag.parse(line)
            cabochaline = tree.toString(CaboCha.FORMAT_LATTICE)

            new.write(cabochaline)

    f.close()
    new.close()



