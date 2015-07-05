#!usr/bin/python
#coding:utf-8

import argparse
import re
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',dest='in_file',default='nlp.txt',help = 'read input file')
    args = parser.parse_args()
    sent = open(args.in_file).read()
    re_pattern = re.compile('[.:;?!](\s)([A-Z])')

    return re_pattern.sub(lambda x: x.group().replace(' ','\n'),sent)





if __name__ == '__main__':
    print main()
