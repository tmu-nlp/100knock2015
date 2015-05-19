# coding:utf-8

import kajiwara_20 as mogura


def main():
    text = mogura.get_country_text(u"イギリス", mogura.get_country())
    category_list = [line.strip() for line in text.split("\n") if line.startswith("[[Category:")]
    print "\n".join([line.split("|")[0].replace("[[Category:", "").replace("]]", "") for line in category_list])


if __name__ == '__main__':
    main()
