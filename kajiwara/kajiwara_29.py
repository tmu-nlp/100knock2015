# coding:utf-8

import re
import json
import urllib
import kajiwara_25 as mogura


def main():
    infobox = mogura.get_infobox(u"イギリス")
    infobox = dict([(key, value.replace("'''''", "").replace("'''", "").replace("''", "")) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"\[\[.*\]\]", lambda x: x.group().replace("[[", "").replace("]]", "").split("|")[0].split("#")[0], value)) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"{{.*}}", lambda x: x.group().replace("{{", "").replace("}}", ""), value)) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"<.*>", "", value)) for key, value in infobox.items()])
    url = "http://ja.wikipedia.org/w/api.php?format=json&action=query&titles=Image:%s&prop=imageinfo&iiprop=url"
    print json.loads(urllib.urlopen(url % infobox["国旗画像"]).read())['query']['pages']['-1']["imageinfo"][0]["url"]


if __name__ == '__main__':
    main()
