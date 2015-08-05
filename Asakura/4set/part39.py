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
for key,value in sorted(mydict.items(),key = lambda x :-x[1]):
    keylist.append(key)
    valuelist.append(value)
#X = keylist
X = range(0,len(valuelist))
Y = valuelist
plt.xlim(1,50)
#plt.xscale('log')
#plt.yscale('log')
plt.loglog(X,Y)#,align='center')
#plt.bar(X,Y,align='center')
plt.show()

