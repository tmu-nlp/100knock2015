# coding:utf-8

import gzip
import json


def get_country():
    dname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/"
    fname = "jawiki-country.json.gz"
    fin = gzip.open(dname + fname, "r")
    json_data = fin.readlines()
    fin.close()
    return [json.loads(json_datum) for json_datum in json_data]


def get_country_text(country, country_list):
    for title_text2data in country_list:
        if title_text2data[u"title"] == country:
            return title_text2data[u"text"].encode("utf-8")
    return None


def main():
    country_list = get_country()
    print get_country_text(u"イギリス", country_list)


if __name__ == '__main__':
    main()
