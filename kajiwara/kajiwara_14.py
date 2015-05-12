# coding:utf-8

import subprocess


def head(fname, number):
    fin = open(fname)
    head_lines = [line.strip() for line in fin][:number]
    fin.close()
    return "\n".join(head_lines)


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    number = 3
    print head(fname, number)
    # 確認
    print "head -%d ../data/hightemp.txt" % number
    subprocess.call("head -" + str(number) + " " + fname, shell=True)


if __name__ == '__main__':
    main()
