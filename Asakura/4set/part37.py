#!usr/bin/python
#--*--coding:utf-8--*--


from part30 import *
from part36 import *
import matplotlib.pyplot as plt
mecablist = makelist()
countdict = count()
keylist = []
valuelist = []
count = 0
for key,value in sorted(countdict.items(),key = lambda x :-x[1]):
    count += 1
    if count == 11:
       break
    keylist.append(key.decode('utf-8'))
    valuelist.append(int(value))

#for i,key,value in zip(range(10),keylist,valuelist):#,key = lambda x:-x[1])):
#    print i,key,value


X = range(1,11)
Y = valuelist
plt.bar(X,Y,align='center')
plt.xticks(X,keylist) # 目盛りを数字から地名に書き換える
plt.title(u'TOP10:頻度')
plt.ylabel(u'頻度')
plt.xlabel(u'単語')
plt.show()
