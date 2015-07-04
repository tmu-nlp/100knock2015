#!usr/bin.python
#--*--coding:utf-8--*--

from part30 import *
from part36 import *
from collections import defaultdict
import matplotlib.pyplot as plt
mydict = defaultdict(lambda :0)
mecablist = makelist()
countdict = count()
for key,value in countdict.items():
    mydict[value] += 1
keylist = []
valuelist = []
for key,value in sorted(mydict.items()):
    keylist.append(key)
    valuelist.append(value)
X = keylist
Y = valuelist
plt.xlim(1,50)
print mydict.keys(),mydict.values()
plt.bar(mydict.keys(),mydict.values(),align='center')
plt.show()

