#coding: utf-8

#def main(x, y, z):
#    text = "%s時の%sは%s" % (x, y, z)
#    return text

#if __name__ == "__main__":
#    x = 12
#    y = "気温"
#    z = 22.4
#    print main(x, y, z)

import sys

def func(x, y, z):
    print "{0}時の{1}は{2}".format(x, y, z)

if __name__ == "__main__":
    (x, y, z) = sys.argv[1:]
    func(x, y, z)
