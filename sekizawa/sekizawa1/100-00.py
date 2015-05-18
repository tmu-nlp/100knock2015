#!/usr/bin/python
list = "stressed"

inv = ""

for i in range(len(list)):
    inv += list[(len(list) - i - 1)]

print inv

