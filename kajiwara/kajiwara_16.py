# coding:utf-8

import subprocess


def split(fname, number):
    fin = open(fname)
    lines, split_lines = (list(), list())
    for i, line in enumerate(fin, start=1):
        lines.append(line.strip())
        if not i % number:
            split_lines.append(lines)
            lines = list()
    if lines:
        split_lines.append(lines)
    fin.close()
    return split_lines


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    fout = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/split_"
    number = 10
    print [len(lines) for lines in split(fname, number)]
    # 確認
    print "split -l%d ../data/hightemp.txt ../data/split_" % number
    subprocess.call("rm " + fout + "*", shell=True)
    subprocess.call("split -l" + str(number) + " " + fname + " " + fout, shell=True)
    subprocess.call("wc -l " + fout + "*", shell=True)


if __name__ == '__main__':
    main()
