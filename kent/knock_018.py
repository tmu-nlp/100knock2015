#coding:utf-8

item = []
i = []
my_file = open("hightemp.txt", "r")
for line in my_file:
    item.append(line.strip().split("\t"))

for i in sorted(item, key = lambda x:x[2], reverse = True):
    print "\t".join(i)
