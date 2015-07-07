#!usr/bin/python
#coding:utf-8


def main(in_file):
    for line in in_file:
        print '\n'.join(line.strip().split(' '))




if __name__ == '__main__':
    f = open ('50result.txt')
    main(f)
