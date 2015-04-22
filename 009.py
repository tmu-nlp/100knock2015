#!user/bin/python
#--*--coding:utf-8--*--

import random
mylist = []
mylist2 = []
mystring = "abcdefg name is ABcdefgHijk"
mylist = mystring.split(" ")

for i in mylist:
  if len(i) > 4:
    array=list(i)
    head = array[0]
    back = array[-1]
    del array[0]
    del array[-1]
    random.shuffle(array)
    array.insert(0,head)
    array.append(back)
    chars="".join(array)
    mylist2.append(chars)
  else:
    mylist2.append(i)
print mylist2
