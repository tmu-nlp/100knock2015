# coding:utf-8

import kajiwara_20 as mogura


def get_infobox(country):
    text = mogura.get_country_text(country, mogura.get_country())
    infobox = [line.strip() for line in text.split("\n}}\n")[0].split("\n") if line.startswith("|")]
    return dict([tuple(line.split("<ref>")[0].replace("|", "").split(" = ")) for line in infobox])


def main():
    infobox = get_infobox(u"イギリス")
    print "\n".join([key+": "+infobox[key] for key in infobox.keys()])


if __name__ == '__main__':
    main()
