#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

for line1, line2 in zip(open(sys.argv[1]), open(sys.argv[2])):#要素を合わせた(行を合わせたリスト)ものをループ
    print '%s\t%s' % (line1.strip(), line2.strip())#line1にcol1の要素が入り、line2にcol2の要素が入る