# coding:utf-8

import subprocess


def wc_l(fname):
    fin = open(fname, "r")
    line_length = len([line for line in fin])
    fin.close()
    return line_length


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    print wc_l(fname)
    # 確認
    print "wc -l ../data/hightemp.txt",
    subprocess.call("wc -l " + fname, shell=True)


if __name__ == '__main__':
    main()
