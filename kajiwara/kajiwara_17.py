# coding:utf-8

import subprocess


def sort_uniq(fname):
    fin = open(fname)
    unique_lines = sorted(list(set([line.strip() for line in fin])))
    fin.close()
    return "\n".join(unique_lines)


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/col1.txt"
    print sort_uniq(fname)
    # 確認
    print "sort ../data/col1.txt | uniq"
    subprocess.call("sort " + fname + " | uniq", shell=True)


if __name__ == '__main__':
    main()
