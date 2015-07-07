# coding:utf-8

import kajiwara_20 as mogura


def main():
    text = mogura.get_country_text(u"イギリス", mogura.get_country())
    print "\n".join([line.strip() for line in text.split("\n") if line.startswith("[[ファイル:")])


if __name__ == '__main__':
    main()
