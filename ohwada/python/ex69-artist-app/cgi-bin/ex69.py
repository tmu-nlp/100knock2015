#!/opt/local/bin/python
# -*- coding:utf-8 -*-

import sys
from pymongo import Connection
import cgi


def create_html():
    html_body = u"""
    <html>
      <head>
        <meta http-equiv="content-type" content=text/html;charset=utf-8" />
      </head>
      <body>
        <form method="POST" action="/cgi-bin/ex69.py">
          アーティスト名、別名、タグ名等を入力！！<br>
           * それぞれ一つだけ<br>
           * 複数種類入れるときはスラッシュで区切る
             （アーティスト名/タグ名 みたいに）<br>
          <input type="text" name="artist_name" size="50" />
          <input type="submit" name="artist_name" value="ポチッと" />
        </form>
      {0}
      </body>
    </html>"""

    return html_body


def create_output(search_results):
    lst = []
    for result in search_results:
        if "name" in result:
            name_output = u"アーティスト名 :  " + result["name"]
        else:
            name_output = u"アーティスト名 :  わかりません！！"
        if "aliases.name" in result:
            aliases_output = u"別名 :  " + result["aliases.name"]
        else:
            aliases_output = u"別名 :  わかりません！！"
        if "begin.date" in result and "end.date" in result:
            date_output = u"活動期間 :  " + result["begin.date"] + "~"\
                                          + result["end.date"]
        else:
            date_output = u"活動期間 :  わかりません！！"
        if "area" in result:
            area_output = u"活動エリア :  " + result["area"]
        else:
            area_output = u"アーティスト名 :  わかりません！！"
        lst.append("\n".join([name_output, aliases_output, date_output, area_output]))

    return u"検索結果...... {0}件<br>".format(str(len(lst))) + "<br>".join(lst)


def search(coll, query_dic):
    artist_name = query_dic.getvalue('artist_name')
    results = coll.find({"name":artist_name[0]})
    output = create_output(results)
    html_body = create_html()
    print "Content-type: text/html;charset=utf-8\n"    
    print html_body.format(output).encode("utf-8")



if __name__ == "__main__":
    conn = Connection('localhost', 27017)
    db = conn.test
    coll = db.artist

    query = cgi.FieldStorage()
    print query
    if not query:
        print "Content-type: text/html;charset=utf-8\n"    
        print create_html().format("").encode("utf-8")
    else:    
        search(coll, query)

