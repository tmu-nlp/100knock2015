#coding: utf-8

str1 = u"パトカー"
str2 = u"タクシー"
new_str = u""

for a, b in zip(str1, str2):
    new_str += a + b

print new_str
