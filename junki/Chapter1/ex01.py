#!/usr/bin/python
#-*-coding:utf-8-*-
str = u"パタトクカシーー"
print str.encode("utf-8")

count = 0
for char in str:
	#print char
	#print count
	if count % 2 == 0:
		print char,
	count += 1

for i in range(len(str)):
	if i % 2 == 1:
		print str[i],

#print str[0:len(a):2]