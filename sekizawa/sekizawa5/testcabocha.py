#!usr/bin/python
#coding:utf-8

import CaboCha

if __name__ == "__main__":

    f = "吾輩は猫である"
    new = open("CaboCha_test.txt.", "w")
    tag = CaboCha.Parser("")

    tree = tag.parse(f.strip())
    print tree.toString(CaboCha.FORMAT_TREE)
    print tree.toString(CaboCha.FORMAT_LATTICE)

    new.write(tree.toString(CaboCha.FORMAT_TREE))
    new.write(tree.toString(CaboCha.FORMAT_LATTICE))

    new.close()




