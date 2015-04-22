#!/usr/bin/python
# _*_ coding: utf-8 _*_

#「パトカー」+ 「タクシー」= 「パタトクカシーー」

pato = u"パトカー"
taku = u"タクシー"
print pato, taku

p_list = list(pato)
t_list = list(taku)
print p_list, t_list

patotaku = []

for index in range(len(p_list)):
    patotaku.append(p_list[index] + t_list[index])  

#for index in range(len(patotaku)):
#     patotaku[index] = str(patotaku[index])
#なぜかできない


patotaku = "".join(patotaku)
print patotaku
