#!/usr/bin/python
from collections import defaultdict

line = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

my_dict = defaultdict(lambda: 0)

words = line.split(" ")

i = 0
for word in words:
    if i == 1 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or                 i == 15 or i == 16 or i == 19:
         my_dict[word[0]] = i
    else:
         my_dict[word[0:2]] = i
    i += 1

print my_dict

