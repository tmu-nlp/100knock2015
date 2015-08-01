#usr/bin/python
#coding:utf-8

import re

def main():
    country_name_list = open('country_name_list')
    train_file = open('part80.txt')
    country_list = list()
    for country in country_name_list:
        country_list.append(country.strip())
    for line in train_file:
        for country in country_list:
            pattern = re.compile('%s'%country)
            line = pattern.sub(lambda x: x.group().replace(' ','_'),line)
        print line




if __name__ == '__main__':
    main()
