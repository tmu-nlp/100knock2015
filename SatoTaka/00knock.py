#!/usr/bin/python
# _*_ coding: utf-8 _*_

#文字列の逆順

original = "stressed"
print original

o_list = list(original)
print o_list

o_list.reverse()
print o_list

o_rev = "".join(o_list)
print o_rev
