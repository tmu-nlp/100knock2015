# coding:utf-8

import subprocess


def paste(fin_name1, fin_name2):
    fin1 = open(fin_name1, "r")
    fin2 = open(fin_name2, "r")
    paste_lines = [line1.strip() + "\t" + line2.strip() for line1, line2 in zip(fin1, fin2)]
    fin1.close()
    fin2.close()
    return "\n".join(paste_lines)


def main():
    fin1 = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/col1.txt"
    fin2 = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/col2.txt"
    print paste(fin1, fin2)
    # 確認
    print "paste ../data/col1.txt ../data/col2.txt"
    subprocess.call("paste " + fin1 + " " + fin2, shell=True)


if __name__ == '__main__':
    main()
