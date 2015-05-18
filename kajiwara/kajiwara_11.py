# coding:utf-8

import subprocess


def sed_e(fname, before, after):
    fin = open(fname, "r")
    replace_lines = [line.strip().replace(before, after) for line in fin]
    fin.close()
    return "\n".join(replace_lines)


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    print sed_e(fname, "\t", " ")
    # 確認
    print "cat ../data/hightemp.txt | sed -e 's/\\t/ /g'"
    subprocess.call("cat " + fname + " | sed -e 's/\t/ /g'", shell=True)


if __name__ == '__main__':
    main()
