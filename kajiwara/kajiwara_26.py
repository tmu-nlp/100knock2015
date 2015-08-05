# coding:utf-8

import kajiwara_25 as mogura


def main():
    infobox = mogura.get_infobox(u"イギリス")
    infobox = dict([(key, value.replace("'''''", "").replace("'''", "").replace("''", "")) for key, value in infobox.items()])
    print "\n".join([key+": "+infobox[key] for key in infobox.keys()])


if __name__ == '__main__':
    main()
