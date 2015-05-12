# coding:utf-8

import subprocess


def sort_r_k(fname, number):
    fin = open(fname)
    sort_lines = sorted([line.strip().split("\t") for line in fin], key=lambda x: x[number - 1], reverse=True)
    sort_lines = ["\t".join(line) for line in sort_lines]
    fin.close()
    return "\n".join(sort_lines)


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    print sort_r_k(fname, 3)
    # 確認
    print "sort -r -k3 ../data/hightemp.txt | uniq"
    subprocess.call("sort -r -k3 " + fname + " | uniq", shell=True)


if __name__ == '__main__':
    main()
