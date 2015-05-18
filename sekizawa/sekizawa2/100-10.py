#!/use/bin/python
#coding: utf-8

if __name__ == "__main__":

    my_file =  open("hightemp.txt", "r")

    i = 0
    for line in my_file:
        i += 1

    print "行数：%d" % (i)

