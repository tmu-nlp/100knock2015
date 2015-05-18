#coding:utf-8

import sys

my_file = open(sys.argv[1], "r")
save_1 = open("col1.txt", "w")
save_2 = open("col2.txt", "w")

for line in my_file:
    item1, item2, item3, item4 = line.strip().split("\t")
    save_1.write(item1+"\n")
    save_2.write(item2+"\n")
    #item = line.strip().split("\t")
    #print item[0]
    #print len(item1.decode("utf-8"))



#print "defaultencoding:", sys.getdefaultencoding()
