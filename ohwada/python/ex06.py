#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import ex05


string1 = "paraparaparadise"
string2 = "paragraph"

   
X = set(ex05.ngram(string1, 2))
Y = set(ex05.ngram(string2, 2))


U = X.union(Y)
I = X.intersection(Y)
D1 = X.difference(Y)
D2 = Y.difference(X)

print "X"
print X
print "Y"
print Y
print "Union"
print U
print "Intersection"
print I
print "Difference(X - Y)"
print D1
print "Difference(Y - X)"
print D2

print ""



t = "se"

if t in X:
    print "X includes 'se'."
else:
    print "X doesn't include 'se'."

if t in Y:
    print "Y includes 'se'."
else:
    print "Y doesn't include 'se'."
