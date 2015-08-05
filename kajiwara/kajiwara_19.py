# coding:utf-8

import subprocess
from collections import defaultdict


def cut_f(field_number, fname):
    fin = open(fname)
    cut_lines = [line.strip().split("\t")[field_number - 1] for line in fin]
    fin.close()
    return cut_lines


def uniq_c(list):
    word2freq = defaultdict(int)
    for word in list:
        word2freq[word] += 1
    return word2freq


def sort_r(object, key_number, reverse_flag):
    if not type(object) == type(list()):
        object = object.items()
    return sorted(object, key=lambda x: x[key_number], reverse=reverse_flag)


def output(word2freq_list):
    print "\n".join([str(freq) + " " + word for word, freq in word2freq_list])


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    output(sort_r(sort_r(uniq_c(cut_f(1, fname)), 0, True), 1, True))
    # 確認
    print "cut -f1 ../data/hightemp.txt | sort | uniq -c | sort -r"
    subprocess.call("cut -f1 " + fname + " | sort | uniq -c | sort -r", shell=True)


if __name__ == '__main__':
    main()
