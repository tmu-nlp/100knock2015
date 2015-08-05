#!usr/bin/python

line1 = "paraparaparadise"
line2 = "paragraph"

X = set()
Y = set()
uni = set()
sxy = set()
syx = set()
mul = set()

for i in range(0, len(line1) - 1):
    X.add(line1[i] + line1[i + 1])

for j in range(0, len(line2) - 1):
    Y.add(line2[j] + line2[j + 1])

uni = X.union(Y)
sxy = X.difference(Y)
syx = Y.difference(X)
mul = X.intersection(Y)

print "X + Y = %s" % uni
print "X - Y = %s" % sxy
print "Y - X = %s" % syx
print "X * Y = %s" % mul


