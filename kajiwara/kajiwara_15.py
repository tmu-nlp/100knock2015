# coding:utf-8

import subprocess


def tail(fname, number):
    fin = open(fname)
    tail_lines = [line.strip() for line in fin][::-1][:number][::-1]
    fin.close()
    return "\n".join(tail_lines)


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    number = 3
    print tail(fname, number)
    # 確認
    print "tail -%d ../data/hightemp.txt" % number
    subprocess.call("tail -" + str(number) + " " + fname, shell=True)


if __name__ == '__main__':
    main()
