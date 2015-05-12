# coding:utf-8

import subprocess


def cut_f(field_number, fin_name, fout_name):
    fin = open(fin_name, "r")
    split_lines = [line.strip().split("\t")[field_number - 1] for line in fin]
    fin.close()
    fout = open(fout_name, "w")
    fout.write("\n".join(split_lines) + "\n")
    fout.close()


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/hightemp.txt"
    fout1 = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/col1.txt"
    fout2 = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/col2.txt"
    cut_f(1, fname, fout1)
    print "col1.txt"
    subprocess.call("cat " + fout1, shell=True)
    print "col2.txt"
    cut_f(2, fname, fout2)
    subprocess.call("cat " + fout2, shell=True)
    # 確認
    print "cut -f1 ../data/hightemp.txt > ../data/col1.txt"
    subprocess.call("cut -f1 " + fname, shell=True)
    print "cut -f2 ../data/hightemp.txt > ../data/col2.txt"
    subprocess.call("cut -f2 " + fname, shell=True)


if __name__ == '__main__':
    main()
