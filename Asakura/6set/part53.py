#!usr/bin/python
#coding:utf-8
import re



def main():
    word_list = list()
    re_pattern = re.compile('<word>(.+?)</word>')
    for line in open('nlp.txt.xml'):
        result = re_pattern.search(line)
        if result is not None:
            word_list.append(result.group(1))
    for word in word_list:
        print word





if __name__ == '__main__':
    main()
