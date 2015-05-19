# coding:utf-8

import kajiwara_20 as mogura


def main():
    text = mogura.get_country_text(u"イギリス", mogura.get_country())
    section_list = [line.strip() for line in text.split("\n") if line.startswith("==")]
    print "\n".join([section+"\t"+str(section.count("=")/2-1) for section in section_list])


if __name__ == '__main__':
    main()
