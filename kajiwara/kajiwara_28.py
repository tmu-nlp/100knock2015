# coding:utf-8

import re
import kajiwara_25 as mogura


def main():
    infobox = mogura.get_infobox(u"イギリス")
    infobox = dict([(key, value.replace("'''''", "").replace("'''", "").replace("''", "")) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"\[\[.*\]\]", lambda x: x.group().replace("[[", "").replace("]]", "").split("|")[0].split("#")[0], value)) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"{{.*}}", lambda x: x.group().replace("{{", "").replace("}}", ""), value)) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"<.*>", "", value)) for key, value in infobox.items()])
    print "\n".join([key+": "+infobox[key] for key in infobox.keys() if infobox[key]])


if __name__ == '__main__':
    main()
